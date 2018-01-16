import Get_Faces as gf
import src.classifier as clf


def run(function, inputfiles_dir, splitfiles_dir, org_model_path, our_model_path):
    gf.run(inputfiles_dir, splitfiles_dir)
    if function == "CLASSIFY":
        clf.run(function, splitfiles_dir, org_model_path, our_model_path)
    if function == "TRAIN":
        clf.run(function, splitfiles_dir, org_model_path, our_model_path)

function = "TRAIN"
inputfiles_dir = '/gt/Idcards/tmp/'
splitfiles_dir = '/gt/Idcards/tmp2/'
org_model_path = 'model/20170512-110547.pb'
our_model_path = 'model/20180109.pkl'

run(function, inputfiles_dir, splitfiles_dir, org_model_path, our_model_path)


