#
# Main Execute file.
# Created On: Tue Oct 01 02:25:17 IST 2019
# Created By: iTM
#
import sys, os
from common.RunSetup import init_evidence_folder, init_log_folder, init_current_data

sys.path.append('./scripts')
init_evidence_folder()
init_log_folder()

init_current_data("993_Configure_Favourites_Add_data")
__import__("1116_Configure_Favourites_Add")
init_current_data("994_Configure_Favourites_Remove_data")
__import__("1117_Configure_Favourites_Remove")
