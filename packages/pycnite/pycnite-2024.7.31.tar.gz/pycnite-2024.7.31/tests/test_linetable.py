# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for pycnite.linetable."""

import itertools
import unittest

from pycnite import bytecode
from pycnite import linetable
from pycnite import mapping
from pycnite import pyc
from pycnite import types

from . import base

class TestLineTable(unittest.TestCase):
    """Test linetable parsing."""

    def _get_linetable(self, testfile, version, fn=None):
        path = base.test_pyc(testfile, version)
        code = pyc.load_file(path)
        if fn is not None:
            code = code.co_consts[fn]
        lt = linetable.linetable_reader(code)
        return lt.read_all()

    def test_read(self):
        src_file = base.test_src("trivial")
        with open(src_file, "r") as f:
            src = f.readlines()
        n_lines = len(src)
        for version in base.VERSIONS:
            entries = self._get_linetable("trivial", version)
            self.assertEqual(entries[-1].line, n_lines)

    def test_flow(self):
        for version in base.VERSIONS:
            entries = self._get_linetable("flow", version)
            lines = [x.line for x in entries]
            lines = [k for k, _ in itertools.groupby(lines)]
            # Lines checked against the godbolt.org disassembler
            if version == (3, 12):
                expected = [0, 1, 2, 3, 4, 2, 1, 5, 6]
            elif version == (3, 11):
                expected = [0, 1, 2, 3, 4, 5, 6, 1, 2]
            elif version == (3, 10):
                expected = [1, 2, 3, 4, 5, 6, 1, 2]
            else:
                expected = [1, 2, 3, 4, 5, 6]
            self.assertEqual(lines, expected, f"version: {version}")

    def test_generator_311(self):
        # Check that we handle NO_COLUMN_INFO correctly in 3.11
        # (regression test for https://github.com/google/pycnite/issues/18)
        entries = self._get_linetable("generator", (3, 11), fn=0)
        self.assertEqual(len(entries), 11)
        for e in entries:
            self.assertEqual(e.line, e.endline)

    def test_read_sequential_311(self):
        """Test sequential get() calls in 3.11+.

        3.11+ combines consecutive opcodes with the same position in a single
        entry in the linetable. This test ensures each opcode reports the
        correct position when read sequentially.
        """
        def pos(e: linetable.Entry):
            return f"{e.line}:{e.startcol}-{e.endline}:{e.endcol}"
        for version in base.VERSIONS:
            if version < (3, 11):
                continue
            opmap = mapping.get_mapping(version)
            path = base.test_pyc("loop", version)
            code = pyc.load_file(path)
            lt = linetable.linetable_reader(code)
            actual = [
                (o.start, opmap[o.op], pos(lt.get(o.start)))
                for o in bytecode.wordcode_reader(code.co_code)
                if o.op != 0  # ignore CACHE entries
            ]
            # Compare to output of:
            # >>> code="""for i in range(10):
            # ...     pass
            # ... """
            # >>> for i in dis.Bytecode(code): print(i.offset, i.positions)
            if version >= (3, 12):
                expected = [
                    (0, "RESUME", "0:0-1:0"),
                    (2, "PUSH_NULL", "1:9-1:14"),
                    (4, "LOAD_NAME", "1:9-1:14"),
                    (6, "LOAD_CONST", "1:15-1:17"),
                    (8, "CALL", "1:9-1:18"),
                    (16, "GET_ITER", "1:0-2:6"),
                    (18, "FOR_ITER", "1:0-2:6"),
                    (22, "STORE_NAME", "1:4-1:5"),
                    (24, "JUMP_BACKWARD", "2:2-2:6"),
                    (26, "END_FOR", "1:0-2:6"),
                    (28, "RETURN_CONST", "1:0-2:6"),
                ]
            else:
                expected = [
                    (0, "RESUME", "0:0-1:0"),
                    (2, "PUSH_NULL", "1:9-1:14"),
                    (4, "LOAD_NAME", "1:9-1:14"),
                    (6, "LOAD_CONST", "1:15-1:17"),
                    (8, "PRECALL", "1:9-1:18"),
                    (12, "CALL", "1:9-1:18"),
                    (22, "GET_ITER", "1:0-2:6"),
                    (24, "FOR_ITER", "1:0-2:6"),
                    (26, "STORE_NAME", "1:4-1:5"),
                    (28, "JUMP_BACKWARD", "2:2-2:6"),
                    (30, "LOAD_CONST", "1:0-2:6"),
                    (32, "RETURN_VALUE", "1:0-2:6"),
                ]
            actual = actual[:len(expected)]
            self.assertEqual(actual, expected, f"version: {version}")


class TestExceptionTable(unittest.TestCase):
    """Test exceptiontable parsing."""

    def test_basic(self):
        for version in base.VERSIONS:
            # Exception table is new in 3.11
            if version < (3, 11):
                continue
            path = base.test_pyc("exception", version)
            code = pyc.load_file(path)
            et = linetable.ExceptionTableReader(code)
            actual = et.read_all()
            entry = types.ExceptionTableEntry
            # Verified using godbolt
            if version == (3, 12):
                expected = [
                    entry(start=4, end=16, target=34, depth=0, lasti=False),
                    entry(start=22, end=30, target=82, depth=0, lasti=False),
                    entry(start=34, end=42, target=66, depth=1, lasti=True),
                    entry(start=44, end=46, target=72, depth=0, lasti=False),
                    entry(start=48, end=54, target=66, depth=1, lasti=True),
                    entry(start=56, end=58, target=72, depth=0, lasti=False),
                    entry(start=60, end=60, target=66, depth=1, lasti=True),
                    entry(start=62, end=70, target=72, depth=0, lasti=False),
                    entry(start=72, end=74, target=76, depth=1, lasti=True),
                    entry(start=82, end=84, target=90, depth=1, lasti=True),
                ]
            else:
                expected = [
                    entry(start=4, end=22, target=26, depth=0, lasti=False),
                    entry(start=24, end=24, target=66, depth=0, lasti=False),
                    entry(start=26, end=34, target=58, depth=1, lasti=True),
                    entry(start=36, end=38, target=66, depth=0, lasti=False),
                    entry(start=40, end=46, target=58, depth=1, lasti=True),
                    entry(start=48, end=50, target=66, depth=0, lasti=False),
                    entry(start=52, end=52, target=58, depth=1, lasti=True),
                    entry(start=54, end=62, target=66, depth=0, lasti=False),
                    entry(start=66, end=68, target=70, depth=1, lasti=True),
                    entry(start=78, end=86, target=92, depth=0, lasti=False),
                    entry(start=92, end=94, target=102, depth=1, lasti=True),
                ]
            self.assertEqual(actual, expected)

    def test_complex(self):
        for version in base.VERSIONS:
            # Exception table is new in 3.11
            if version < (3, 11):
                continue
            path = base.test_pyc("complex_exception", version)
            code = pyc.load_file(path)
            et = linetable.ExceptionTableReader(code.co_consts[0])
            actual = et.read_all()
            entry = types.ExceptionTableEntry
            # Verified using godbolt
            if version == (3, 12):
                expected = [
                    entry(start=8, end=18, target=138, depth=0, lasti=False),
                    entry(start=20, end=76, target=78, depth=1, lasti=True),
                    entry(start=78, end=86, target=96, depth=3, lasti=True),
                    entry(start=88, end=134, target=138, depth=0, lasti=False),
                    entry(start=138, end=154, target=242, depth=1, lasti=True),
                    entry(start=156, end=220, target=232, depth=1, lasti=True),
                    entry(start=232, end=240, target=242, depth=1, lasti=True),
                ]
            else:
                expected = [
                    entry(start=8, end=20, target=162, depth=0, lasti=False),
                    entry(start=22, end=94, target=96, depth=1, lasti=True),
                    entry(start=96, end=102, target=104, depth=3, lasti=True),
                    entry(start=104, end=108, target=162, depth=0, lasti=False),
                    entry(start=110, end=110, target=104, depth=3, lasti=True),
                    entry(start=112, end=158, target=162, depth=0, lasti=False),
                    entry(start=162, end=180, target=286, depth=1, lasti=True),
                    entry(start=182, end=264, target=276, depth=1, lasti=True),
                    entry(start=276, end=284, target=286, depth=1, lasti=True),
                ]
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
