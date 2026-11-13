# Tests for estimate_store.py - Sprint 2
# These tests use a throwaway file, never the real estimates.json,
# so the real saved list is never touched.
# Run them with: py -m pytest


from estimate_store import EstimateStore         # IMPORT - brings in the store class to test


def test_load_missing_file_gives_empty_list(tmp_path):   # FUNCTION - tests loading when no file exists yet; tmp_path is a fresh empty folder pytest makes for this test
    test_file = tmp_path / "test_estimates.json"   # VARIABLE - a test file path inside that fresh folder
    store = EstimateStore(str(test_file))          # VARIABLE = OBJECT - a store that looks after the test file
    assert store.load() == []                      # assert - checks that no file yet means an empty list


def test_save_then_load_gives_same_list(tmp_path):   # FUNCTION - tests saving and then reading back
    test_file = tmp_path / "test_estimates.json"   # VARIABLE - a test file path inside a fresh folder
    store = EstimateStore(str(test_file))          # VARIABLE = OBJECT - a store that looks after the test file
    estimates = [{"name": "Test", "squares": 20, "total": 8500}]   # VARIABLE = LIST - one estimate to save
    store.save(estimates)                          # FUNCTION CALL - writes the list into the test file
    assert store.load() == estimates               # assert - checks that reading it back gives the same list


def test_save_empty_list_then_load(tmp_path):      # FUNCTION - tests saving an empty list
    test_file = tmp_path / "test_estimates.json"   # VARIABLE - a test file path inside a fresh folder
    store = EstimateStore(str(test_file))          # VARIABLE = OBJECT - a store that looks after the test file
    store.save([])                                 # FUNCTION CALL - writes an empty list into the test file
    assert store.load() == []                      # assert - checks that reading it back gives an empty list


def test_save_two_estimates_then_load(tmp_path):   # FUNCTION - tests saving a list with two estimates
    test_file = tmp_path / "test_estimates.json"   # VARIABLE - a test file path inside a fresh folder
    store = EstimateStore(str(test_file))          # VARIABLE = OBJECT - a store that looks after the test file
    estimates = [{"name": "Test", "squares": 20, "total": 8500}, {"name": "Maria", "squares": 2, "total": 3000}]   # VARIABLE = LIST - two estimates to save
    store.save(estimates)                          # FUNCTION CALL - writes the list into the test file
    loaded = store.load()                          # VARIABLE - reads the list back from the test file
    assert len(loaded) == 2                        # assert - checks that two estimates came back
    assert loaded[1]["name"] == "Maria"            # assert - checks the second estimate kept its name


def test_save_again_replaces_old_list(tmp_path):   # FUNCTION - tests that saving again replaces the old list
    test_file = tmp_path / "test_estimates.json"   # VARIABLE - a test file path inside a fresh folder
    store = EstimateStore(str(test_file))          # VARIABLE = OBJECT - a store that looks after the test file
    store.save([{"name": "Old", "squares": 1, "total": 100}])   # FUNCTION CALL - saves a first list
    store.save([{"name": "New", "squares": 2, "total": 200}])   # FUNCTION CALL - saves a second list over the first
    loaded = store.load()                          # VARIABLE - reads the list back from the test file
    assert loaded == [{"name": "New", "squares": 2, "total": 200}]   # assert - checks that only the new list is there
