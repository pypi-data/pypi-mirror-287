import os
import unittest

from nose.plugins import PluginTester  # type: ignore

from pynose_exclude import PynoseExclude


class TestPynoseExcludeDirs_Relative_Args(PluginTester, unittest.TestCase):
    """Test pynose-exclude directories using relative paths passed
    on the commandline via --exclude-dir
    """

    activate = "--exclude-dir=test_dirs/build"
    args = ['--exclude-dir=test_dirs/test_not_me']
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output


class TestPynoseExcludeDirs_Absolute_Args(PluginTester, unittest.TestCase):
    """Test pynose-exclude directories using absolute paths passed
    on the commandline via --exclude-dir
    """

    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def __init__(self, *args, **kwargs):
        self.activate = "--exclude-dir=%s" % \
                        os.path.join(self.suitepath, 'build')
        arg_path = os.path.join(self.suitepath, 'test_not_me')
        self.args = ['--exclude-dir=%s' % arg_path]
        super(TestPynoseExcludeDirs_Absolute_Args, self).__init__(*args, **kwargs)

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output


class TestPynoseExcludeDirs_Relative_Args_File(PluginTester, unittest.TestCase):
    """Test pynose-exclude directories using relative paths passed
    by file using --exclude-dir-file
    """

    activate = "--exclude-dir-file=test_dirs/exclude_dirs.txt"
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output


class TestPynoseExcludeDirs_Relative_Args_Mixed(PluginTester, unittest.TestCase):
    """Test pynose-exclude directories using paths passed
    by file and commandline
    """

    activate = "--exclude-dir-file=test_dirs/exclude_dirs2.txt"
    args = ["--exclude-dir=test_dirs/test_not_me"]
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output


class TestPynoseExcludeEnvVariables(PluginTester, unittest.TestCase):
    """Test pynose-exclude's use of environment variables"""

    # args = ['--exclude-dir=test_dirs/test_not_me']
    activate = "-v"
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    env = {'PYNOSE_EXCLUDE_DIRS': 'test_dirs/build;test_dirs/test_not_me'}

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output


class TestPynoseExcludeDirsEnvFile(PluginTester, unittest.TestCase):
    """Test pynose-exclude directories using relative paths passed
    by file specified by environment variable
    """

    activate = "-v"
    plugins = [PynoseExclude()]
    env = {'PYNOSE_EXCLUDE_DIRS_FILE': 'test_dirs/exclude_dirs.txt'}
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output


class TestPynoseExcludeDirs_Arg_Does_Not_Exist(PluginTester, unittest.TestCase):
    """Test pynose-exclude directories for a directory that doesn't exist.
    """

    activate = "--exclude-dir=test_dirs/build"
    args = ["--exclude-dir=test_dirs/test_not_me \n --exclude-dir=test_dirs/test_i_dont_exist"]
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output


class TestPynoseExcludeDirsPynoseWorkingDir(PluginTester, unittest.TestCase):
    """Test pynose-exclude directories with Pynose's working directory."""

    activate = "--exclude-dir=test_not_me"
    args = ["--where=test_dirs"]
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def tearDown(self):
        # Pynose changes cwd to config.workingDir, need to reset it
        import os
        os.chdir(os.path.join(os.getcwd(), os.path.pardir))

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output


class TestPynoseExcludeTest(PluginTester, unittest.TestCase):
    """Test pynose-exclude a single test"""

    activate = "--exclude-test=test_dirs.unittest.tests.UnitTests.test_a"
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_test_excluded(self):
        assert 'Ran 2 tests' in self.output


class TestPynoseExcludeTestNegative(PluginTester, unittest.TestCase):
    """Test pynose-exclude a test that does not exist"""

    activate = "--exclude-test=test_dirs.unittest.tests.UnitTests.does_not_exist"
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_test_excluded_negative(self):
        assert 'Ran 3 tests' in self.output


class TestPynoseExcludeTestsEnvVariables(PluginTester, unittest.TestCase):
    """Test pynose-exclude's use of environment variables"""

    activate = "-v"
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')
    env = {
        'PYNOSE_EXCLUDE_TESTS':
            'test_dirs.unittest.tests.UnitTests.test_a;'
            'test_dirs.unittest.tests.test_c'
    }

    def test_test_excluded(self):
        assert 'Ran 1 test' in self.output


class TestPynoseExcludeMultipleTest(PluginTester, unittest.TestCase):
    """Test pynose-exclude multiple tests"""

    activate = "--exclude-test=test_dirs.unittest.tests.UnitTests.test_a"
    args = [
        "--exclude-test=test_dirs.unittest.tests.UnitTests.test_b",
        "--exclude-test=test_dirs.unittest.tests.test_c"
    ]
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_tests_excluded(self):
        assert 'Ran 0 tests' in self.output


class TestPynoseExcludeTestViaFile(PluginTester, unittest.TestCase):
    """Test pynose-exclude tests with a file"""

    activate = "--exclude-test-file=test_dirs/exclude_tests.txt"
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_tests_excluded(self):
        assert 'Ran 1 test' in self.output


class TestPynoseExcludeDirAndTests(PluginTester, unittest.TestCase):
    """Test pynose-exclude tests by specifying dirs and tests"""

    activate = "--exclude-test=test_dirs.unittest.tests.UnitTests.test_a"
    args = [
        "--exclude-dir=test_dirs/build",
        "--exclude-dir=test_dirs/build2",
        "--exclude-dir=test_dirs/fish",
        "--exclude-dir=test_dirs/test_not_me",
        "--exclude-dir=test_dirs/test_yes",
        "--exclude-dir=test_dirs/test_yes2",
    ]
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def test_tests_excluded(self):
        assert 'Ran 2 tests' in self.output


class TestPynoseExcludeTestClass(PluginTester, unittest.TestCase):
    """Test pynose-exclude tests by class"""

    activate = "--exclude-test=test_dirs.unittest.tests.UnitTests"
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_tests_excluded(self):
        assert 'Ran 1 test' in self.output


class TestPynoseExcludeTestFunction(PluginTester, unittest.TestCase):
    """Test pynose-exclude tests by function"""

    activate = "--exclude-test=test_dirs.unittest.tests.test_c"
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_tests_excluded(self):
        assert 'Ran 2 tests' in self.output


class TestPynoseExcludeTestModule(PluginTester, unittest.TestCase):
    """Test pynose-exclude tests by module"""

    activate = "--exclude-test=test_dirs.unittest.test"
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_tests_excluded(self):
        assert 'Ran 3 tests' in self.output


class TestPynoseDoesNotExcludeTestClass(PluginTester, unittest.TestCase):
    """Test pynose-exclude tests by class"""

    activate = "--exclude-test=test_dirs.unittest.test"
    plugins = [PynoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_tests_not_excluded(self):
        assert 'Ran 3 tests' in self.output


if __name__ == '__main__':
    unittest.main()
