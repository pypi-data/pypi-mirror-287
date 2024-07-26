import os
from typing import Any, Dict, List, Optional, Generator, Tuple, TYPE_CHECKING

from datetime import datetime
from modal.volume import FileEntry
from warnings import warn

#import logging
#logger = logging.getLogger("modal_or_local." + __name__)

if TYPE_CHECKING:
    from modal_or_local import ModalOrLocal


class ModalOrLocalDir:
    """Class to do directory things and sync between modal volumes and/or local filesystems"""

    def __init__(
        self,
        dir_full_path: str,
        modal_or_local: Optional["ModalOrLocal"] = None,
        volume_name: Optional[str] = None,
        volume_mount_dir: Optional[str] = None,
    ):
        """Expects dir_full_path and either modal_or_local or (volume_name and volume_mount_dir) to be passed"""
        self.dir_full_path = os.path.normpath(dir_full_path)
        """Full path of the directory - should include volume mount if on a volume"""

        from modal_or_local import ModalOrLocal

        # Set self.modal_or_local
        if modal_or_local:
            self.modal_or_local = modal_or_local
            """The ModalOrLocal instance designating the modal volume or local filesystem on which our directory lives"""
            if volume_name:
                warn(
                    volume_name
                    + " is ignored when a ModalOrLocal instance (modal_or_local) is passed"
                )
            if volume_mount_dir:
                warn(
                    volume_mount_dir
                    + " is ignored when a ModalOrLocal instance (modal_or_local) is passed"
                )

        elif volume_name and volume_mount_dir:
            self.modal_or_local = ModalOrLocal(
                volume_name=volume_name, volume_mount_dir=volume_mount_dir
            )
        elif volume_name or volume_mount_dir:
            raise ValueError(
                f"Expected both volume_name and volume_mount_dir to be set if either is passed. Got {volume_name=}, {volume_mount_dir=}"
            )
        else:
            # Will be using the local filesystem
            self.modal_or_local = ModalOrLocal()

        # If the directory is on a modal volume, make sure the path includes the volume mount dir
        if (
            self.modal_or_local.volume
            and not self.modal_or_local.path_starts_with_volume_mount_dir(
                self.dir_full_path
            )
        ):
            raise RuntimeError(
                f"ModalOrLocalDir in volume full path expected to start with volume mount dir {self.modal_or_local.volume_name=}, {self.dir_full_path=}"
            )

    def volume_mount_dir(self):
        """Return a the modal_or_local.volume_mount_dir"""
        return self.modal_or_local.volume_mount_dir

    def volume(self):
        """Return a the modal_or_local.volume"""
        return self.modal_or_local.volume

    def get_full_path(self, filename: str) -> str:
        """Prepend the directory path to the given filename. File may or may not exist"""
        return os.path.join(self.dir_full_path, filename)

    def __str__(self):
        return (
            __class__.__name__
            + f"(dir_full_path={self.dir_full_path}, modal_or_local={self.modal_or_local})"
        )

    def listdir(
        self, relative_path: str = None, return_full_paths: bool = False
    ) -> List[str]:
        """Return a (non-recursive) list of files/directories in the given path. For recursive see walk()"""

        if relative_path:
            if relative_path.startswith("/"):
                raise RuntimeError(
                    f"Expected relative path to be relative, but got absolute: {relative_path=}"
                )

            return self.modal_or_local.listdir(
                os.path.join(self.dir_full_path, relative_path),
                return_full_paths=return_full_paths,
            )
        else:
            return self.modal_or_local.listdir(
                self.dir_full_path, return_full_paths=return_full_paths
            )

    def write_json_file(
        self, json_file_relative_path: str, metadata: Any, force: bool = True
    ):
        """Write a json file to the directory. This will overwrite existing and create any needed parent/sub directories automatically."""
        return self.modal_or_local.write_json_file(
            new_json_file_full_path=self.get_full_path(json_file_relative_path),
            metadata=metadata,
            force=force,
        )

    def read_json_file(self, json_file_relative_path: str) -> Any:
        """Load json from the given file"""
        return self.modal_or_local.read_json_file(
            json_file_full_path=self.get_full_path(json_file_relative_path)
        )

    def write_file(
        self, new_file_relative_path: str, encoded_content: Any, force: bool = True
    ):
        """Write the encoded content to a file in either the local filesystem or to a volume. This will create any needed parent directories automatically."""
        return self.modal_or_local.write_file(
            new_file_full_path=self.get_full_path(new_file_relative_path),
            encoded_content=encoded_content,
            force=force,
        )

    def read_file(self, file_relative_path: str) -> Any:
        """Load content from the given file"""
        return self.modal_or_local.read_file(
            file_full_path=self.get_full_path(file_relative_path)
        )

    def file_or_dir_exists(self, file_relative_path: str) -> bool:
        """Returns true if the passed file or directory exists in our directory"""
        return self.modal_or_local.file_or_dir_exists(
            full_path=self.get_full_path(file_relative_path)
        )

    def isfile(self, file_relative_path: str) -> bool:
        """Returns true if the passed file exists in our directory"""
        return self.modal_or_local.isfile(
            full_path=self.get_full_path(file_relative_path)
        )

    def isdir(self, dir_relative_path: str) -> bool:
        """Returns true if the passed directory exists in our directory"""
        return self.modal_or_local.isdir(
            full_path=self.get_full_path(dir_relative_path)
        )

    def get_mtime(self, file_relative_path: str) -> float:
        """Returns modified time (in seconds since epoch) of the given file/dir in our directory"""
        return self.modal_or_local.get_mtime(
            full_path=self.get_full_path(file_relative_path)
        )

    def get_FileEntry(self, file_relative_path: str) -> FileEntry:
        """Return a modal.volume.FileEntry for the given path (relative to our directory) if it exists."""
        return self.modal_or_local.get_FileEntry(
            full_path=self.get_full_path(file_relative_path)
        )

    def remove_file_or_directory(self, relative_path: str, dne_ok: bool = False):
        """Remove the given relative path (file or directory) from the filesystem or modal volume"""
        return self.modal_or_local.remove_file_or_directory(
            file_or_dir_to_remove_full_path=self.get_full_path(relative_path),
            dne_ok=dne_ok,
        )

    def remove_own_directory(self, dne_ok: bool = False):
        """Remove the ModalOrLocalDir object's directory (self.dir_full_path) from the filesystem or modal volume"""
        return self.modal_or_local.remove_file_or_directory(
            self.dir_full_path, dne_ok=dne_ok
        )

    def walk(self) -> Generator[Tuple[str, list[str], list[str]], None, None]:
        """
        Return a generator of (dirpath, dirs, files) tuples similar to os.walk(). Uses os.walk() if not using a volume and running locally.
        Note dirpath will include the volume_mount_dir if applicable.

        Yields:
            Tuple[str, list[str], list[str]]: A tuple containing the current directory path,
            a list of subdirectory names, and a list of filenames.
        """
        yield self.modal_or_local.walk(dir_full_path=self.dir_full_path)

    def report_changes(self, since_datetime: Optional[datetime] = None) -> Dict:
        """Return files/dirs that have changed in this directory since the given datetime (inclusive)
        Note this tries to give changed directories as well, but the mtimes changing on modal volume directories seems to be unreliable (maybe caching?).
        It will catch new directories but may or may not catch changed ones (ones with new/modified entries)"""

        report = {
            "new_or_modified_files": [],
            "new_or_modified_directories": [],
        }

        if since_datetime is None:
            # Everything is considered new
            # print(f"Walking without since_datetime {self.dir_full_path=}")
            for path, dirs, files in self.modal_or_local.walk(self.dir_full_path):
                # print(f"Walking {path=}, {dirs=}, {files=}")
                for file in files:
                    report["new_or_modified_files"].append(os.path.join(path, file))
                for dir in dirs:
                    report["new_or_modified_directories"].append(
                        os.path.join(path, dir)
                    )
        else:
            # Check for changes since the since_datetime
            # print(f"Walking {since_datetime.timestamp()=} {self.dir_full_path=}")
            for path, dirs, files in self.modal_or_local.walk(self.dir_full_path):
                # print(f"Walking {path=}, {dirs=}, {files=}")
                for file in files:
                    full_path = os.path.join(path, file)
                    mtime = self.modal_or_local.get_mtime(full_path)
                    # print(f"  mtime of file {full_path} is {mtime}")
                    if mtime >= since_datetime.timestamp():
                        # print("  adding file", full_path, mtime-since_datetime.timestamp())
                        report["new_or_modified_files"].append(full_path)

                for dir in dirs:
                    full_path = os.path.join(path, dir)
                    mtime = self.modal_or_local.get_mtime(full_path)
                    if mtime >= since_datetime.timestamp():
                        report["new_or_modified_directories"].append(full_path)

        return report

    def copy_changed_files_from(
        self, source_mdir: "ModalOrLocalDir", since_date: datetime = None
    ) -> List[str]:
        """Copy files/dirs that have changed since the given date (if specified) and are newer than what is currently in this directory.
        Returns list of the relative paths of the files that were copied"""

        changes = source_mdir.report_changes(since_date)

        copied_files = []
        for file_full_path in changes.get("new_or_modified_files"):
            # See if this file exists already in the destination
            file_relative_path = str(file_full_path).replace(
                source_mdir.dir_full_path + "/", ""
            )
            existing_mtime = self.get_mtime(file_relative_path)
            source_mtime = source_mdir.get_mtime(file_relative_path)

            if existing_mtime is None or existing_mtime < source_mtime:
                # print(f"Will copy {file_relative_path}, {existing_mtime=} {source_mtime=} diff of {source_mtime-existing_mtime if existing_mtime else 'n/a'}")
                self.copy_file(
                    source_mdir=source_mdir,
                    source_file_relative_path=file_relative_path,
                    destination_relative_path=file_relative_path,
                )
                copied_files.append(file_relative_path)

            # else:
            # print(f"Will skip {file_relative_path} since it is not newer: {existing_mtime=} {source_mtime=} diff of {source_mtime-existing_mtime if existing_mtime else 'n/a'}")

        return copied_files

    def copy_file(
        self,
        source_mdir: "ModalOrLocalDir",
        source_file_relative_path: str,
        destination_relative_path: Optional[str] = None,
    ):
        """Copy a file from source_mdir/source_file_relative_path to the destination path in this directory.
        If destination_relative_path is an existing directory or ends with '/' the file will be of the same name and placed in that directory.
        If destination_relative_path is None or blank, the file will be copied to the same relative path it has at the source.
        Otherwise the file will be named according to the basename of destination_relative_path.
        """
        if not destination_relative_path:
            destination_relative_path = source_file_relative_path

        from modal_or_local.modal_or_local_copy import copy_file

        copy_file(
            source_mocal=source_mdir.modal_or_local,
            source_file_full_path=source_mdir.get_full_path(source_file_relative_path),
            destination_mocal=self.modal_or_local,
            destination_full_path=self.get_full_path(destination_relative_path),
        )
