#%%
from .ExperimentBase import Experiment
from .DataExtractor import EDEMDataExtractor
# from ExtractKinematics import ExtractKinematics

from .extract_contacts_v2 import ExtractContacts
#from extract_contacts_mp import ExtractContacts
from .LoadExperimentData import ExpData

from .visualisation import Visualisation
import os

#dem_folder_path = '/media/deniz/CommonStorage/Datasets/EDEMv2/collision_box/'
#name = 'exp_4'
#exp = Experiment(exp_path=dem_folder_path,name=name)

def extract(dem_folder_path,name, contact_video=True, animate_deck=True):
    exp = Experiment(exp_path=dem_folder_path,name=name)
    DATASET_FOLDER = dem_folder_path
    SUB_FOLDERS = ["particles", "metadata", "gifs", "contacts", "energy"]
    SUBSUBFOLDERS = ["positions", "velocities", "forces", "energy"]

    for folder in SUB_FOLDERS:
        os.makedirs(os.path.join(DATASET_FOLDER, folder), exist_ok=True)
    for subfolder in SUBSUBFOLDERS:
        os.makedirs(os.path.join(DATASET_FOLDER, "particles", subfolder), exist_ok=True)
    os.makedirs(os.path.join(DATASET_FOLDER, "contacts", "videos"), exist_ok=True)
    extractor = EDEMDataExtractor(exp)
    extractor.saveSystemEnergy()
    extractor.save_material_properties()
    extractor.saveParticleProperties()
    extractor.save_kinematics()
    contacts = ExtractContacts(exp)
    contacts.savecontacts()
    if contact_video or animate_deck:
        positions = ExpData(exp).positions
        visualisation = Visualisation(exp, positions)
        if animate_deck:
            print("saving animation of the deck")
            visualisation.animate_deck(save=True, show=True)
        if contact_video:
            print("saving contact video")
            p2p, p2g = contacts.read_contacts()
            visualisation.contact_video(p2p, p2g, save=True, start_step=1, fps=30)
    print(f"Extracting {exp.name} is done")

