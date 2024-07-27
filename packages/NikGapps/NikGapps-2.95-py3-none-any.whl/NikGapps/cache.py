import os
from dotenv import load_dotenv
from NikGapps.build.Build import Build
from NikGapps.config.NikGappsConfig import NikGappsConfig
from NikGapps.helper.Package import Package
from NikGapps.helper.compression.Modes import Modes
from NikGapps.helper.compression.CompOps import CompOps
from NikGapps.helper.AppSet import AppSet
from NikGapps.helper import Config
from NikGapps.helper.P import P
from NikGapps.helper.T import T
from NikGapps.helper.SystemStat import SystemStat
from NikGapps.helper.Args import Args
from NikGapps.helper.git.GitOperations import GitOperations


def cache():
    args = Args()
    print("Start of the Program")
    SystemStat.show_stats()
    P.green("---------------------------------------")
    load_dotenv()
    Config.ENVIRONMENT_TYPE = os.getenv("ENVIRONMENT_TYPE") if os.getenv("ENVIRONMENT_TYPE") else "production"
    Config.RELEASE_TYPE = os.getenv("RELEASE_TYPE") if os.getenv("RELEASE_TYPE") else "stable"
    android_versions = [Config.TARGET_ANDROID_VERSION]
    Config.UPLOAD_FILES = args.upload
    if len(args.get_android_versions()) > 0:
        android_versions = args.get_android_versions()
    print("---------------------------------------")
    print("Android Versions to build: " + str(android_versions))
    print("---------------------------------------")
    for android_version in android_versions:
        arch = "arm64"
        repo_cached = GitOperations.clone_apk_source(android_version, arch=arch, release_type=Config.RELEASE_TYPE,
                                                     cached=True)
        GitOperations.clone_apk_source(android_version, args.arch, release_type=Config.RELEASE_TYPE)
        GitOperations.clone_overlay_repo(android_version=str(android_version), fresh_clone=True)
        config_obj = NikGappsConfig(android_version)
        app_set_list = config_obj.package_manager.get_packages("all")
        config_obj.config_package_list = Build.build_from_directory(app_set_list, android_version, arch)
        for appset in config_obj.config_package_list:
            appset: AppSet
            for pkg in appset.package_list:
                pkg: Package
                compression_modes = [Modes.ZIP, Modes.TAR_XZ]
                for mode in compression_modes:
                    t = T()
                    print(f"Compressing into {mode} {pkg.package_title} for {appset.title}")
                    pkg_zip_path = os.path.join(repo_cached.working_tree_dir, appset.title,
                                                f"{pkg.package_title}{mode}")
                    print("Done!") if CompOps.compress_package(pkg_zip_path, pkg, mode) else print("Failed!")
                    t.taken(f"Total time taken to process the {pkg.package_title}, compressing into {mode}")
                repo_cached.git_push(commit_message=f"Compressed {pkg.package_title} for {appset.title}",
                                     push_untracked_files=True, pull_first=True, post_buffer="1048576000")


if __name__ == "__main__":
    cache()
