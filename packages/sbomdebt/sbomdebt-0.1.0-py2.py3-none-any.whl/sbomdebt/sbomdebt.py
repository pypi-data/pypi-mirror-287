
from lib4sbom.parser import SBOMParser
from lib4sbom.data.package import SBOMPackage
from lib4package.metadata import Metadata
from packageurl import PackageURL

class SBOMDebt:

    def __init__(self, sbom):
        self.sbom = sbom

    def calculate(self):

        def get_package_info(package_name, package_type, version):
            package_metadata = Metadata(package_type)
            package_metadata.get_package(package_name)
            latest_version = package_metadata.get_latest_version()
            latest_date = package_metadata.get_latest_release_time()
            updates = package_metadata.get_no_of_updates(version)
            return latest_version, latest_date, updates

        # Set up SBOM parser
        test_parser = SBOMParser()
        # Load SBOM - will autodetect SBOM type
        test_parser.parse_file(self.sbom)
        pack = SBOMPackage()
        for p in test_parser.get_packages():
            pack.initialise()
            pack.copy_package(p)
            purl = pack.get_purl()
            if purl is not None:
                purl_info = PackageURL.from_string(purl).to_dict()
                latest_version, latest_date, updates = get_package_info(purl_info["name"], purl_info["type"], purl_info["version"])
                if updates > 2:
                    print (f"Latest version {latest_version}. {updates} updates available for {purl_info['name']}.")
                #elif updates == 0 and latest_version != purl_info['version']:
                #    print (f"Version mismatch for {purl_info['name']}. Current version {purl_info['version']}. Latest version {latest_version}")




