#
# Main Execute file.
# Created On: Mon Sep 30 09:15:22 IST 2019
# Created By: iTM
#
import sys, os
from common.RunSetup import init_evidence_folder, init_log_folder, init_current_data

sys.path.append('./scripts')
init_evidence_folder()
init_log_folder()

init_current_data("989_Configure_Favourites_Add_data")
__import__("1113_Configure_Favourites_Add")
init_current_data("990_Configure_Favourites_Remove_data")
__import__("1112_Configure_Favourites_Remove")
