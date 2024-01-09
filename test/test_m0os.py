import pytest 
import os
import m0py.m0os as m0os

# Test 1: Opening a file in an existing path
def test_open_existing_path():
    # Ensure the path exists
    os.makedirs('test_dir', exist_ok=True)
    with m0os.m0open('test_dir/test_file.txt', 'w') as f:
        f.write("Hello World")
    assert os.path.exists('test_dir/test_file.txt')

# Test 2: Opening a file where the path needs to be created
def test_open_non_existing_path():
    if os.path.exists('new_test_dir'):
        os.rmdir('new_test_dir')
    with m0os.m0open('new_test_dir/test_file.txt', 'w') as f:
        f.write("Hello World")
    assert os.path.exists('new_test_dir/test_file.txt')

# Test 3: Handling errors (e.g., invalid mode)
def test_open_with_invalid_mode():
    with pytest.raises(ValueError):
        with m0os.m0open('test_dir/test_file.txt', 'invalid_mode') as f:
            f.write("Hello World")

# Clean up test files and directories after tests
def teardown_module(module):
    os.path.isfile('test_dir/test_file.txt') and os.remove('test_dir/test_file.txt')
    os.rmdir('test_dir')
    os.path.isfile('new_test_dir/test_file.txt') and os.remove('new_test_dir/test_file.txt')
    os.rmdir('new_test_dir')
