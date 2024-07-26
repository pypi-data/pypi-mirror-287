import modal
import json
import os
from modal_or_local import setup_image, ModalOrLocal
from modal_or_local.modal_or_local_copy import copy, copy_dir, copy_file

# Call this with 'modal run tests/test_modal_or_local_dir.py'
# PRW todo - write custom runner for pytest to run this?

image = setup_image()
app = modal.App("test_modal_or_local_dir")

mvol1 = ModalOrLocal(
    volume_name="test_modal_or_local_copy_volume_one",
    volume_mount_dir="/test_mnt_dir_one",
)
mvol2 = ModalOrLocal(
    volume_name="test_modal_or_local_copy_volume_two",
    volume_mount_dir="/test_mnt_dir_two",
)
mlocal = ModalOrLocal()

#
# Copy file tests. Test modal_or_local_copy.copy_file()
#


@app.function(image=image, volumes={mvol1.volume_mount_dir: mvol1.volume})
def test_copy_local_file_to_volume():
    """Copy a file from local filesystem to a volume. Tests modal_or_local_copy.copy_file()"""

    print(
        "\n\nRunning test_copy_local_to_volume",
        "locally" if modal.is_local() else "remotely",
    )

    if not modal.is_local():
        raise RuntimeError(
            "Cannot run test_copy_local_file_to_volume remotely since /tmp is not mounted"
        )

    # Create the test file locally
    temp_dir_name = "test_copy_local_file_to_volume_dir"
    temp_dir_local = os.path.join("/tmp", temp_dir_name)
    os.makedirs(temp_dir_local, exist_ok=True)

    test_json_data = json.loads('{"a":1, "b":2}')
    test_file_full_path_local = os.path.join(temp_dir_local, "test.json")
    mlocal.write_json_file(test_file_full_path_local, test_json_data)

    assert mlocal.file_or_dir_exists(
        test_file_full_path_local
    ), f"Count not find file created locally {test_file_full_path_local=}"

    # Set the name of the directory that will be used on the volume
    temp_dir_volume_one = os.path.join(mvol1.volume_mount_dir, temp_dir_name)

    # Copy the file from the local filesystem to the modal volume, naming the destination file explicitly
    destination_file_full_path = os.path.join(
        temp_dir_volume_one, "named_dest_test.json"
    )
    copy_file(
        source_mocal=mlocal,
        source_file_full_path=test_file_full_path_local,
        destination_mocal=mvol1,
        destination_full_path=destination_file_full_path,
    )

    # Make sure the file was copied over and contains the expected info
    assert mvol1.file_or_dir_exists(
        destination_file_full_path
    ), f"Could not find named file copied to volume {destination_file_full_path=}"
    read_data = mvol1.read_json_file(destination_file_full_path)
    assert read_data is not None
    assert read_data.get("a") == 1
    assert read_data.get("b") == 2

    # Copy the file from the local filesystem to the modal volume, naming the destination directory
    destination_directory = os.path.join(temp_dir_volume_one)
    copy_file(
        source_mocal=mlocal,
        source_file_full_path=test_file_full_path_local,
        destination_mocal=mvol1,
        destination_full_path=destination_directory,
    )

    # Make sure the file was copied over and contains the expected info
    destination_file_full_path = os.path.join(destination_directory, "test.json")
    assert mvol1.file_or_dir_exists(
        destination_file_full_path
    ), f"Could not find file copied to volume dir {destination_file_full_path=}"
    read_data = mvol1.read_json_file(destination_file_full_path)
    assert read_data is not None
    assert read_data.get("a") == 1
    assert read_data.get("b") == 2

    # Remove the temporary dirs and verify they are gone
    mlocal.remove_file_or_directory(temp_dir_local)
    mvol1.remove_file_or_directory(temp_dir_volume_one)
    assert not mlocal.file_or_dir_exists(temp_dir_local)
    assert not mvol1.file_or_dir_exists(temp_dir_volume_one)
    print(
        "Running test_copy_local_to_volume",
        "locally" if modal.is_local() else "remotely",
        "finished",
    )


@app.function(
    image=image,
    volumes={
        mvol1.volume_mount_dir: mvol1.volume,
        mvol2.volume_mount_dir: mvol2.volume,
    },
)
def test_copy_file_from_volume_to_volume():
    """Copy a file from one volume to another. Tests modal_or_local_copy.copy_file()"""
    print(
        "\n\nRunning test_copy_file_from_volume_to_volume",
        "locally" if modal.is_local() else "remotely",
    )

    # Set the name of the temporary directories that will be used on volumes one and two
    temp_dir_name = "test_copy_file_from_volume_to_volume_dir"
    temp_dir_volume_one = os.path.join(mvol1.volume_mount_dir, temp_dir_name)
    temp_dir_volume_two = os.path.join(mvol2.volume_mount_dir, temp_dir_name)

    # Create a json file on volume one
    test_json_data = json.loads('{"a":1, "b":2}')
    test_file_full_path_volume1 = os.path.join(temp_dir_volume_one, "test.json")
    mvol1.write_json_file(test_file_full_path_volume1, test_json_data)

    assert mvol1.file_or_dir_exists(
        test_file_full_path_volume1
    ), f"Count not find file created on volume one {test_file_full_path_volume1=}"

    # Copy the file from volume one to volume two, naming the destination file explicitly
    destination_file_full_path = os.path.join(
        temp_dir_volume_two, "named_dest_test.json"
    )
    copy_file(
        source_mocal=mvol1,
        source_file_full_path=test_file_full_path_volume1,
        destination_mocal=mvol2,
        destination_full_path=destination_file_full_path,
    )

    # Make sure the file was copied over to volume two and contains the expected info
    assert mvol2.file_or_dir_exists(
        destination_file_full_path
    ), f"Could not find named file copied to volume {destination_file_full_path=}"
    read_data = mvol2.read_json_file(destination_file_full_path)
    assert read_data is not None
    assert read_data.get("a") == 1
    assert read_data.get("b") == 2

    # Copy the file from modal volume one to modal volume2, naming the destination directory
    destination_directory = os.path.join(temp_dir_volume_two)
    copy_file(
        source_mocal=mvol1,
        source_file_full_path=test_file_full_path_volume1,
        destination_mocal=mvol2,
        destination_full_path=destination_directory,
    )

    # Make sure the file was copied over to volume two and contains the expected info
    destination_file_full_path = os.path.join(destination_directory, "test.json")
    assert mvol2.file_or_dir_exists(
        destination_file_full_path
    ), f"Could not find file copied to volume dir {destination_file_full_path=}"
    read_data = mvol2.read_json_file(destination_file_full_path)
    assert read_data is not None
    assert read_data.get("a") == 1
    assert read_data.get("b") == 2

    # Remove the temporary dirs and verify they are gone
    mvol1.remove_file_or_directory(temp_dir_volume_one)
    mvol2.remove_file_or_directory(temp_dir_volume_two)
    assert not mvol1.file_or_dir_exists(temp_dir_volume_one)
    assert not mvol2.file_or_dir_exists(temp_dir_volume_two)
    print(
        "Running test_copy_file_from_volume_to_volume",
        "locally" if modal.is_local() else "remotely",
        "finished",
    )


@app.function(image=image, volumes={mvol1.volume_mount_dir: mvol1.volume})
def test_copy_file_from_volume_to_local():
    """Copy a file from a modal volume to the local filesystem. Tests modal_or_local_copy.copy_file()"""
    print(
        "\n\nRunning test_copy_file_from_volume_to_local",
        "locally" if modal.is_local() else "remotely",
    )

    if not modal.is_local():
        raise RuntimeError(
            "Cannot run test_copy_file_from_volume_to_local remotely since /tmp is not mounted"
        )

    # Set the name of the temporary directories that will be used on volumes one and two
    temp_dir_name = "test_copy_file_from_volume_to_local_dir"
    temp_dir_volume_one = os.path.join(mvol1.volume_mount_dir, temp_dir_name)
    temp_dir_local = os.path.join("/tmp", temp_dir_name)
    os.makedirs(temp_dir_local, exist_ok=True)

    # Create a json file on volume one
    test_json_data = json.loads('{"a":11, "b":22}')
    test_file_full_path_volume1 = os.path.join(temp_dir_volume_one, "test.json")
    mvol1.write_json_file(test_file_full_path_volume1, test_json_data)

    assert mvol1.file_or_dir_exists(
        test_file_full_path_volume1
    ), f"Count not find file created on volume one {test_file_full_path_volume1=}"

    # Copy the file from volume one to local filesystem, naming the destination file explicitly
    destination_file_full_path = os.path.join(temp_dir_local, "named_dest_test.json")
    copy_file(
        source_mocal=mvol1,
        source_file_full_path=test_file_full_path_volume1,
        destination_mocal=mlocal,
        destination_full_path=destination_file_full_path,
    )

    # Make sure the file was copied to the local filesystem and contains the expected info
    assert mlocal.file_or_dir_exists(
        destination_file_full_path
    ), f"Could not find named file copied to local {destination_file_full_path=}"
    read_data = mlocal.read_json_file(destination_file_full_path)
    assert read_data is not None
    assert read_data.get("a") == 11
    assert read_data.get("b") == 22

    # Copy the file from modal volume one to modal volume2, naming the destination directory
    destination_directory = temp_dir_local
    copy_file(
        source_mocal=mvol1,
        source_file_full_path=test_file_full_path_volume1,
        destination_mocal=mlocal,
        destination_full_path=destination_directory,
    )

    # Make sure the file was copied over to volume two and contains the expected info
    destination_file_full_path = os.path.join(destination_directory, "test.json")
    assert mlocal.file_or_dir_exists(
        destination_file_full_path
    ), f"Could not find file copied to local dir {destination_file_full_path=}"
    read_data = mlocal.read_json_file(destination_file_full_path)
    assert read_data is not None
    assert read_data.get("a") == 11
    assert read_data.get("b") == 22

    # Remove the temporary dirs and verify they are gone
    mvol1.remove_file_or_directory(temp_dir_volume_one)
    mlocal.remove_file_or_directory(temp_dir_local)
    assert not mvol1.file_or_dir_exists(temp_dir_volume_one)
    assert not mlocal.file_or_dir_exists(temp_dir_local)
    print(
        "Running test_copy_file_from_volume_to_local",
        "locally" if modal.is_local() else "remotely",
        "finished",
    )


#
# Copy directory tests.  Test modal_or_local_copy.copy_dir()
#


@app.function(image=image, volumes={mvol1.volume_mount_dir: mvol1.volume})
def test_copy_dir_from_local_to_volume():
    """Copy a populated directory from the local filesystem to a modal volume. Tests modal_or_local_copy.copy_dir()"""

    print(
        "\n\nRunning test_copy_dir_from_local_to_volume",
        "locally" if modal.is_local() else "remotely",
    )

    if not modal.is_local():
        raise RuntimeError(
            "Cannot run test_copy_dir_from_local_to_volume remotely since /tmp is not mounted remotely"
        )

    # Set the name of the temporary directories that will be used locally and on volume one
    temp_dir_name = "test_copy_dir_from_local_to_volume_dir"
    temp_dir_volume_one = os.path.join(mvol1.volume_mount_dir, temp_dir_name)
    # Start fresh
    if mvol1.file_or_dir_exists(temp_dir_volume_one):
        mvol1.remove_file_or_directory(temp_dir_volume_one)

    # print(f"{temp_dir_volume_one=}")
    temp_dir_local = os.path.join("/tmp", temp_dir_name)
    os.makedirs(temp_dir_local, exist_ok=True)

    # Create a file tree locally
    # /tmp/test_copy_dir_from_local_to_volume_dir
    # ├── a.json
    # ├── b.json
    # ├── c.json
    # ├── empty_subdir
    # └── subdir
    #     ├── aa.json
    #     ├── bb.json
    #     └── cc.json

    expected_files_relative_path = []  # relative path of expected files

    # Create a.json, b.json, c.json in /tmp/test_copy_dir_from_local_to_volume_dir
    for prefix in ["a", "b", "c"]:
        test_json_data = json.loads(
            '{"' + prefix + '": "' + prefix + '_val"}'
        )  # e,g. {"a":"a_val"}
        test_file_full_path_local = os.path.join(temp_dir_local, prefix + ".json")

        # Create the file
        mlocal.write_json_file(test_file_full_path_local, test_json_data)
        # Make sure the file got created
        assert mlocal.file_or_dir_exists(
            test_file_full_path_local
        ), f"Could not find file created on local {test_file_full_path_local=}"
        # Track that we expect this file
        expected_files_relative_path.append(os.path.basename(test_file_full_path_local))

    # Create aa.json, bb.json, cc.json in /tmp/test_copy_dir_from_local_to_volume_dir/subdir
    for prefix in ["aa", "bb", "cc"]:
        test_json_data = json.loads(
            '{"' + prefix + '": "' + prefix + '_val"}'
        )  # e,g. {"aa":"aa_val"}
        test_file_full_path_local = os.path.join(
            temp_dir_local, "subdir", prefix + ".json"
        )
        # Create the file
        mlocal.write_json_file(test_file_full_path_local, test_json_data)

        # Make sure the file got created
        assert mlocal.file_or_dir_exists(
            test_file_full_path_local
        ), f"Could not find file created on local {test_file_full_path_local=}"

        # Track that we expect this file
        expected_files_relative_path.append(
            os.path.join("subdir", os.path.basename(test_file_full_path_local))
        )

    # Add /tmp/test_copy_file_from_local_to_volume_dir/empty_subdir as an empty dir
    test_empty_dir_full_path_local = os.path.join(temp_dir_local, "empty_subdir")
    mlocal.create_directory(test_empty_dir_full_path_local)
    expected_files_relative_path.append("empty_subdir")

    # print ("Expected files:\n", "\n".join(expected_files_relative_path))

    # Copy the directory from local filesystem to modal volume.
    # The volume one temp dir does not yet exist so it will be created as the copy of the local temporary dir
    copy_dir(
        source_mocal=mlocal,
        source_dir_full_path=temp_dir_local,
        destination_mocal=mvol1,
        destination_full_path=temp_dir_volume_one,
    )

    # Make sure the expected files all exist
    for file_relative_path in expected_files_relative_path:
        full_path = os.path.join(temp_dir_volume_one, file_relative_path)
        assert mvol1.file_or_dir_exists(
            full_path
        ), f"Could not locate expected {full_path=}"

    # Remove the temporary dirs and verify they are gone
    mvol1.remove_file_or_directory(temp_dir_volume_one)
    mlocal.remove_file_or_directory(temp_dir_local)
    assert not mvol1.file_or_dir_exists(
        temp_dir_volume_one
    ), f"Failed to remove {temp_dir_volume_one=}"
    assert not mlocal.file_or_dir_exists(
        temp_dir_local
    ), f"Failed to remove {temp_dir_local=}"
    print(
        "Running test_copy_dir_from_local_to_volume",
        "locally" if modal.is_local() else "remotely",
        "finished",
    )


@app.function(image=image, volumes={mvol1.volume_mount_dir: mvol1.volume})
def test_copy_dir_from_volume_to_local():
    """Copy a populated directory from a volume to the local filesystem. Tests modal_or_local_copy.copy_dir()"""
    print(
        "\n\nRunning test_copy_dir_from_volume_to_local",
        "locally" if modal.is_local() else "remotely",
    )

    if not modal.is_local():
        raise RuntimeError(
            "Cannot run test_copy_dir_from_volume_to_local remotely since /tmp is not mounted remotely"
        )

    # Set the name of the temporary directories that will be used locally and on volumes one
    temp_dir_name = "test_copy_dir_from_volume_to_local_dir"
    temp_dir_volume_one = os.path.join(mvol1.volume_mount_dir, temp_dir_name)
    # print(f"{temp_dir_volume_one=}")
    temp_dir_local = os.path.join("/tmp", temp_dir_name)
    os.makedirs(temp_dir_local, exist_ok=True)

    # Create a file tree on volume one
    # /test_mnt_dir_one/test_copy_file_from_volume_to_local_dir:         a.json,  b.json,  c.json
    # /test_mnt_dir_one/test_copy_file_from_volume_to_local_dir/subdir: aa.json, bb.json, cc.json
    # /test_mnt_dir_one/test_copy_file_from_volume_to_local_dir/empty_subdir <empty>
    expected_files_relative_path = []  # relative path (from mount dir) of expected files

    # Create a.json, b.json, c.json in /test_mnt_dir_one/test_copy_file_from_volume_to_local_dir
    for prefix in ["a", "b", "c"]:
        test_json_data = json.loads(
            '{"' + prefix + '": "' + prefix + '_val"}'
        )  # e,g. {"a":"a_val"}
        test_file_full_path_volume_one = os.path.join(
            temp_dir_volume_one, prefix + ".json"
        )
        mvol1.write_json_file(test_file_full_path_volume_one, test_json_data)
        assert mvol1.file_or_dir_exists(
            test_file_full_path_volume_one
        ), f"Could not find file created on volume one {test_file_full_path_volume_one=}"
        expected_files_relative_path.append(
            os.path.basename(test_file_full_path_volume_one)
        )

    # Create aa.json, bb.json, cc.json in /test_mnt_dir_one/test_copy_file_from_volume_to_local_dir/subdir
    for prefix in ["aa", "bb", "cc"]:
        test_json_data = json.loads(
            '{"' + prefix + '": "' + prefix + '_val"}'
        )  # e,g. {"aa":"aa_val"}
        test_file_full_path_volume_one = os.path.join(
            temp_dir_volume_one, "subdir", prefix + ".json"
        )
        mvol1.write_json_file(test_file_full_path_volume_one, test_json_data)
        assert mvol1.file_or_dir_exists(
            test_file_full_path_volume_one
        ), f"Count not find file created on local {test_file_full_path_volume_one=}"
        expected_files_relative_path.append(
            os.path.join("subdir", os.path.basename(test_file_full_path_volume_one))
        )

    # Add /test_mnt_dir_one/test_copy_file_from_volume_to_local_dir/empty_subdir as an empty dir
    test_empty_dir_full_path_volume_one = os.path.join(
        temp_dir_volume_one, "empty_subdir"
    )
    mvol1.create_directory(test_empty_dir_full_path_volume_one)
    expected_files_relative_path.append("empty_subdir")

    # print ("Expected files:\n", "\n".join(expected_files_relative_path))

    # Copy the directory from the modal volume to the local filesystem.
    # Note that temp_dir_local already exists, so a copy of the "test_copy_file_from_volume_to_local_dir" directory will be placed inside of it
    copy_dir(
        source_mocal=mvol1,
        source_dir_full_path=temp_dir_volume_one,
        destination_mocal=mlocal,
        destination_full_path=temp_dir_local,
    )

    # Make sure the expected files all exist
    for file_relative_path in expected_files_relative_path:
        assert mlocal.file_or_dir_exists(
            os.path.join(temp_dir_local, temp_dir_name, file_relative_path)
        )

    # Remove the temporary dirs and verify they are gone
    mvol1.remove_file_or_directory(temp_dir_volume_one)
    mlocal.remove_file_or_directory(temp_dir_local)
    assert not mvol1.file_or_dir_exists(temp_dir_volume_one)
    assert not mlocal.file_or_dir_exists(temp_dir_local)
    print(
        "Running test_copy_dir_from_volume_to_local",
        "locally" if modal.is_local() else "remotely",
        "finished",
    )


#
#  Copy tests. Test modal_or_local_copy.copy()
#


@app.function(
    image=image,
    volumes={
        mvol1.volume_mount_dir: mvol1.volume,
        mvol2.volume_mount_dir: mvol2.volume,
    },
)
def test_copy():
    """Copy a file between volumes, then a populated directory between volumes. Tests modal_or_local_copy.copy()"""

    print("Running test_copy", "locally" if modal.is_local() else "remotely", "started")
    # Set the name of the temporary directories that will be used on volumes one and two
    temp_dir_name = "test_copy"
    temp_dir_volume_one = os.path.join(mvol1.volume_mount_dir, temp_dir_name)
    temp_dir_volume_two = os.path.join(mvol2.volume_mount_dir, temp_dir_name)

    # Copy a file from volume one to volume two

    # Create a json file on volume one
    test_json_data = json.loads('{"a":7, "b":8}')
    test_file_full_path_volume1 = os.path.join(temp_dir_volume_one, "test.json")
    mvol1.write_json_file(test_file_full_path_volume1, test_json_data)

    assert mvol1.file_or_dir_exists(
        test_file_full_path_volume1
    ), f"Count not find file created on volume one {test_file_full_path_volume1=}"

    # Copy the file from volume one to volume two, naming the destination file explicitly
    destination_file_full_path = os.path.join(
        temp_dir_volume_two, "named_dest_test.json"
    )
    copy(
        source_mocal=mvol1,
        source_path=test_file_full_path_volume1,
        destination_mocal=mvol2,
        destination_path=destination_file_full_path,
    )

    # Make sure the file was copied over to volume two and contains the expected info
    assert mvol2.file_or_dir_exists(
        destination_file_full_path
    ), f"Could not find named file copied to volume {destination_file_full_path=}"
    read_data = mvol2.read_json_file(destination_file_full_path)
    assert read_data is not None
    assert read_data.get("a") == 7
    assert read_data.get("b") == 8

    # Copy a directory from volume two to volume one

    # Create a.json, b.json, c.json on volume two in /test_mnt_dir_two/test_copy
    expected_files_relative_path = []
    dir_to_copy_full_path_volume_two = os.path.join(temp_dir_volume_two, "subdir")
    for prefix in ["a", "b", "c"]:
        test_json_data = json.loads(
            '{"' + prefix + '": "' + prefix + '_val"}'
        )  # e,g. {"a":"a_val"}
        test_file_full_path_volume_two = os.path.join(
            dir_to_copy_full_path_volume_two, prefix + ".json"
        )
        mvol2.write_json_file(test_file_full_path_volume_two, test_json_data)
        assert mvol2.file_or_dir_exists(
            test_file_full_path_volume_two
        ), f"Could not find file created on volume two {test_file_full_path_volume_two=}"
        expected_files_relative_path.append(
            test_file_full_path_volume_two.replace(temp_dir_volume_two + "/", "", 1)
        )

    copy(
        source_mocal=mvol2,
        source_path=dir_to_copy_full_path_volume_two,
        destination_mocal=mvol1,
        destination_path=temp_dir_volume_one,
    )

    # Make sure the expected files all exist
    for file_relative_path in expected_files_relative_path:
        test_file_full_path_volume_one = os.path.join(
            temp_dir_volume_one, file_relative_path
        )
        print(f"{test_file_full_path_volume_one=}")
        assert mvol1.file_or_dir_exists(
            test_file_full_path_volume_one
        ), f"Did not find file on volume one: {test_file_full_path_volume_one=}"

    print(
        "Running test_copy", "locally" if modal.is_local() else "remotely", "finished"
    )


#
# Main - call the tests. Run this using 'modal run test_modal_or_local_copy.py'
#


@app.local_entrypoint()
def main():
    test_copy_local_file_to_volume.local()
    test_copy_file_from_volume_to_volume.local()
    test_copy_file_from_volume_to_volume.remote()
    test_copy_file_from_volume_to_local.local()
    test_copy_dir_from_local_to_volume.local()
    test_copy_dir_from_volume_to_local.local()
    test_copy.local()
    test_copy.remote()
