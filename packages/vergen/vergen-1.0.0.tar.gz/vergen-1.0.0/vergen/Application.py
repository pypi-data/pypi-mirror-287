import argparse
import hashlib
import os
import subprocess

class Application:
    def __init__(self):
        self.name = "vergen"
        self.description = "vergen is a version generator which uses git tags to generate a branch-dependent version."
        self.version = "1.0.0"

    def run(self):
        parser = argparse.ArgumentParser(prog=self.name, description=self.description)
        parser.add_argument("--version", action="version", version=f"%(prog)s {self.version}")
        parser.add_argument("--verbose", action="store_true", help="print verbose information")

        args = parser.parse_args()

        if not self.__is_git_working_directory():
            raise RuntimeError("Current working directory is not a git-controlled directory.")

        branch = self.__get_active_branch()
        tag = self.__get_latest_tag()
        commit_count = self.__get_commit_count_since_tag(tag)
        version = self.__generate_version(branch, tag, commit_count)

        if args.verbose:
            print(f"Active branch: {branch}")
            print(f"Latest tag: {tag}")
            print(f"Commits since tag: {commit_count}")
            print(f"Generated version: {version}")
        else:
            print(version)

    def __is_git_working_directory(self):
        return os.path.exists(".git")

    def __get_active_branch(self):
        try:
            result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return result.stdout.decode("utf-8").strip()
        except Exception:
            raise RuntimeError("Cannot find the active branch.")

    def __get_latest_tag(self):
        try:
            result = subprocess.run(["git", "describe", "--tags", "--match", f"[0-9]*.[0-9]*"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            tag_with_commit_info = result.stdout.decode("utf-8").strip()
            # Extract only the tag part without the additional commit information
            tag_parts = tag_with_commit_info.split("-")
            return tag_parts[0]
        except Exception:
            raise RuntimeError("Cannot find the latest tag.")

    def __get_commit_count_since_tag(self, tag):
        try:
            result = subprocess.run(["git", "rev-list", f"{tag}..HEAD", "--count"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return int(result.stdout.decode("utf-8").strip())
        except Exception:
            raise RuntimeError("Cannot count commits since the latest tag.")

    def __generate_version(self, branch, major_minor, commit_count):
        if branch in {"main", "master"}:
            return f"{major_minor}.{commit_count}"
        elif branch == "develop":
            branch_id = 1
        elif branch.startswith("hotfix/"):
            branch_id = self.__hash(branch, 10, 99)
        elif branch.startswith("release/"):
            branch_id = self.__hash(branch, 100, 999)
        elif branch.startswith("feature/"):
            branch_id = self.__hash(branch, 1000, 9999)
        else:
            raise RuntimeError(f"Unexpected branch: {branch}")
        
        return f"{major_minor}.{commit_count}.{branch_id}"
    
    def __hash(self, branch, min_version, max_version):
        count = max_version - min_version + 1
        return int(hashlib.sha256(branch.encode()).hexdigest(), 16) % count + min_version
