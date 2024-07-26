import modal
import json
import os
from datetime import datetime
from modal_or_local import setup_image, ModalOrLocal

# Call this with 'modal run tests/test_modal_or_local.py'
# PRW todo - write custom runner for pytest to run this?

image = setup_image()
app = modal.App("test_modal_or_local")

mocal = ModalOrLocal(
    volume_name="test_modal_or_local_volume", volume_mount_dir="/test_mnt_dir"
)


@app.function(image=image, volumes={mocal.volume_mount_dir: mocal.volume})
def test_write_and_read_volume_json_file():
    """Write a json file to a modal volume then read it (should be able to run both .local() and .remote())"""

    print(
        "Running test_read_file_from_volume",
        "locally" if modal.is_local() else "remotely",
    )
    test_json_data = json.loads('{"a":1, "b":2}')

    json_file_full_path = os.path.join(
        mocal.volume_mount_dir, "test_write_and_read_volume_json_file.json"
    )

    mocal.write_json_file(json_file_full_path, test_json_data, force=True)

    assert mocal.file_or_dir_exists(json_file_full_path)

    read_data = mocal.read_json_file(json_file_full_path)
    assert read_data is not None
    assert read_data.get("a") == 1
    assert read_data.get("b") == 2

    # Remove the test file
    mocal.remove_file_or_directory(json_file_full_path)

    # Check that file was actually deleted
    assert not mocal.file_or_dir_exists(json_file_full_path)

    print(
        "Running test_read_file_from_volume",
        "locally" if modal.is_local() else "remotely",
        "finished",
    )


@app.function(image=image, volumes={mocal.volume_mount_dir: mocal.volume})
def test_write_and_read_volume_txt_file():
    """Write a text file to a modal volume then read it (should be able to run both .local() and .remote())"""

    print(
        "Running test_write_and_read_volume_txt_file",
        "locally" if modal.is_local() else "remotely",
    )

    file_full_path = os.path.join(
        mocal.volume_mount_dir, "test_write_and_read_volume_txt_file.txt"
    )
    text_to_encode = "This is some text"

    mocal.write_file(file_full_path, text_to_encode.encode(), force=True)

    assert mocal.file_or_dir_exists(file_full_path)

    content = mocal.read_file(file_full_path)
    file_text = content.decode("utf-8")

    assert file_text is not None
    assert file_text == text_to_encode

    # Remove the test file
    mocal.remove_file_or_directory(file_full_path)

    # Cannot check that file was actually deleted without a reload of the volume, not sure how to use reload() (get running function error) so commenting out
    assert not mocal.file_or_dir_exists(file_full_path)

    print(
        "Running test_write_and_read_volume_txt_file",
        "locally" if modal.is_local() else "remotely",
        "finished",
    )


@app.function(image=image, volumes={mocal.volume_mount_dir: mocal.volume})
def test_create_or_remove_dir():
    """Create and remove directory within a volume"""
    for dir_to_create in [
        "test_create_or_remove_dir_data",
        "/test_create_or_remove_dir_data/test/a/b/c",
    ]:
        if dir_to_create.startswith("/"):
            dir_to_create = dir_to_create.replace("/", "")
        dir_to_create_full_path = os.path.join(mocal.volume_mount_dir, dir_to_create)
        # print(f"Creating '{dir_to_create_full_path=}'")
        mocal.create_directory(dir_to_create_full_path)
        assert mocal.file_or_dir_exists(dir_to_create_full_path)
        mocal.remove_file_or_directory(dir_to_create_full_path)
        assert not mocal.file_or_dir_exists(dir_to_create_full_path)


@app.function(image=image, volumes={mocal.volume_mount_dir: mocal.volume})
def test_listdir():
    """Create files in a temp directory, then read the list of files in the directory"""
    temp_dir = os.path.join(mocal.volume_mount_dir, "test_listdir_data")
    mocal.remove_file_or_directory(temp_dir, dne_ok=True)
    mocal.create_directory(temp_dir)

    # Add some files to the temp directory on the volume
    filenames_created = []
    for prefix in ["a", "b", "c"]:
        filename = prefix + ".txt"
        filenames_created.append(filename)
        full_path = os.path.join(temp_dir, filename)
        file_text = "some text for file " + prefix
        mocal.write_file(full_path, file_text.encode())

    # List the directory and check that all of the expected files are in the list
    found_filenames = mocal.listdir(temp_dir)

    assert (
        len(found_filenames) == len(filenames_created)
    ), f"Expected {len(filenames_created)} files but found {len(found_filenames)}. {filenames_created=} {found_filenames=}"
    # print(f"{found_filenames=}")
    for filename in filenames_created:
        assert filename in found_filenames, (
            "Expected filename '"
            + filename
            + "' not found in listdir "
            + str(found_filenames)
        )

    # List the directory with full path option and check that all of the expected files are in the list
    found_filenames_full_path = mocal.listdir(temp_dir, return_full_paths=True)
    # print(f"{found_filenames_full_path=}")
    for filename in filenames_created:
        full_path = os.path.join(temp_dir, filename)
        assert full_path in found_filenames_full_path, (
            "Expected full path "
            + full_path
            + " not found in listdir "
            + str(found_filenames_full_path)
        )

    # Add a subdirectory "subdir"
    subdir_filenames_created = []
    for prefix in ["aa", "bb", "cc"]:
        subdir_filenames_created.append(prefix + ".txt")
        full_path = os.path.join(temp_dir, "subdir", prefix + ".txt")
        file_text = "some text for subdir file " + prefix
        mocal.write_file(full_path, file_text.encode())

    found_subdir_filenames = mocal.listdir(os.path.join(temp_dir, "subdir"))
    assert (
        len(found_subdir_filenames) == len(subdir_filenames_created)
    ), f"Expected {len(subdir_filenames_created)} files but found {len(found_subdir_filenames)}. {subdir_filenames_created=} {found_filenames=}"
    # print(f"{found_filenames=}")
    for filename in subdir_filenames_created:
        assert (
            filename in found_subdir_filenames
        ), f"Expected filename '{filename}' not found in listdir.  {subdir_filenames_created=} {found_subdir_filenames=}"

    # Now that there is a subdir, make sure the original listing still works (does not report anything recursive)
    found_filenames = mocal.listdir(temp_dir)
    filenames_created.append("subdir")

    assert (
        len(found_filenames) == len(filenames_created)
    ), f"Expected {len(filenames_created)} files but found {len(found_filenames)}. {filenames_created=} {found_filenames=}"
    # print(f"{found_filenames=}")
    for filename in filenames_created:
        assert (
            filename in found_filenames
        ), f"Expected filename '{filename}' not found in listdir: {filenames_created=} {found_filenames=}"

    # Try listing just a file
    file_full_path = os.path.join(temp_dir, "a.txt")
    assert (
        mocal.listdir(file_full_path) == ["a.txt"]
    ), f"Expected mocal.listdir({file_full_path}) to give ['a.txt'] but got {mocal.listdir(file_full_path)=}"
    # Remove the temp test dir
    mocal.remove_file_or_directory(temp_dir)


@app.function(image=image, volumes={mocal.volume_mount_dir: mocal.volume})
def test_walk():
    """Create files/dirs in a temp directory, then walk the list of files in the directory"""
    temp_dir = os.path.join(mocal.volume_mount_dir, "test_walk_data")
    mocal.create_directory(temp_dir)
    second_level_dir = os.path.join(temp_dir, "mydir")
    mocal.create_directory(second_level_dir)

    expected_tuples = []

    # Add some files to the temp directory on the volume
    filenames_created = []
    # Add some files to the temp_dir
    for prefix in ["a", "b", "c"]:
        filename = prefix + ".txt"
        full_path = os.path.join(temp_dir, filename)
        file_text = "this is some text in file " + prefix
        mocal.write_file(full_path, file_text.encode())
        filenames_created.append(filename)
    expected_tuples.append(
        (temp_dir, [os.path.basename(second_level_dir)], filenames_created)
    )

    # Add some files to temp_dir/second_level_dir
    filenames_created = []
    for prefix in ["aa", "bb", "cc"]:
        filename = prefix + ".txt"
        full_path = os.path.join(second_level_dir, filename)
        file_text = "this is some text in file " + prefix
        mocal.write_file(full_path, file_text.encode())
        filenames_created.append(filename)
    expected_tuples.append((second_level_dir, [], filenames_created))

    walk_tuples = []
    for tup in mocal.walk(temp_dir):
        walk_tuples.append(tup)

    # print(f"{expected_tuples=}")
    # print(f"{walk_tuples=}")

    assert walk_tuples_equal(walk_tuples, expected_tuples)

    # Remove the temp test dir
    mocal.remove_file_or_directory(temp_dir)


def convert_walk_tuple_lists_to_sets(tuples):
    return [(t[0], frozenset(t[1]), frozenset(t[2])) for t in tuples]


def walk_tuples_equal(expected, actual) -> bool:
    from collections import Counter

    expected_converted = convert_walk_tuple_lists_to_sets(expected)
    actual_converted = convert_walk_tuple_lists_to_sets(actual)
    return Counter(expected_converted) == Counter(actual_converted)


@app.function(image=image, volumes={mocal.volume_mount_dir: mocal.volume})
def test_get_FileEntry():
    """Create a file and dir on the volume, check we can get FileEntry of each"""
    temp_dir = os.path.join(
        mocal.volume_mount_dir, "test_get_FileEntry", "second_level_dir"
    )
    mocal.create_directory(temp_dir)
    json_file_full_path = os.path.join(temp_dir, "mytest.json")
    mocal.write_json_file(json_file_full_path, {"x": 1, "y": 2})

    for path in [
        mocal.volume_mount_dir,
        f"{mocal.volume_mount_dir}/test_get_FileEntry",
        f"{mocal.volume_mount_dir}/test_get_FileEntry",
        temp_dir,
        json_file_full_path,
    ]:
        entry = mocal.get_FileEntry(path)
        # print(f"mocal.get_FileEntry({path})=", mocal.get_FileEntry(path), "\n\n")

        # entry.path will not have a leading slash, so remove from path before testing equality
        if path != "/" and path.startswith("/"):
            path = path.replace("/", "", 1)
        assert (
            entry.path == path
        ), f"Expected '{path}' but got '{entry.path}' from {entry}"

    for path in ["a", "mytest.json", "second_level_dir"]:
        path_to_check = os.path.join(mocal.volume_mount_dir, path)
        assert not mocal.get_FileEntry(
            full_path=path_to_check
        ), f"Expected None but got {entry}"

    # Remove the temp test dir
    mocal.remove_file_or_directory(temp_dir)


@app.function(image=image, volumes={mocal.volume_mount_dir: mocal.volume})
def test_get_mtime():
    # Define our temp dir for this test and make sure it does not yet exist
    temp_dir = os.path.join(mocal.volume_mount_dir, "test_get_mtime_data")
    if mocal.file_or_dir_exists(temp_dir):
        mocal.remove_file_or_directory(temp_dir)  # start fresh

    json_file_full_path = os.path.join(temp_dir, "test_get_mtime.json")
    mocal.write_json_file(json_file_full_path, {"x": 1})

    now_in_seconds = int(datetime.now().timestamp())
    # print(f"{now_in_seconds=}")

    mtime = mocal.get_mtime(json_file_full_path)
    # print(f"         {mtime=}")
    assert (
        abs(now_in_seconds - mtime) < 3
    ), f"Expected mtime to be within three seconds of now but got {abs(now_in_seconds - mtime)}s, {mtime=}, {now_in_seconds=}"

    # Get the mtime from the new json file and compare to now


@app.function(image=image, volumes={mocal.volume_mount_dir: mocal.volume})
def test_get_time_delta():
    mocal_for_local = ModalOrLocal()
    time_delta = mocal_for_local.get_time_delta(mocal=mocal)
    time_delta_reverse = mocal.get_time_delta(mocal=mocal_for_local)
    print(f"{time_delta=} {time_delta_reverse=}")


@app.local_entrypoint()
def main():
    print("Running", __file__, "locally" if modal.is_local() else "remotely")

    test_write_and_read_volume_json_file.local()
    test_write_and_read_volume_json_file.remote()
    test_create_or_remove_dir.local()
    test_create_or_remove_dir.remote()
    test_write_and_read_volume_txt_file.local()
    test_write_and_read_volume_txt_file.remote()
    test_listdir.local()
    test_listdir.remote()
    test_walk.local()
    test_walk.remote()
    test_get_FileEntry.local()
    test_get_FileEntry.remote()
    test_get_mtime.local()
    test_get_mtime.remote()
    test_get_time_delta.local()
