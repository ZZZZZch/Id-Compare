import src.align.align_dataset_mtcnn as align

# input_dir = '/gt/Idcards/org'
# output_dir = "/gt/Idcards/org_split"

def run(input_dir, output_dir):
    align.main(align.parse_arguments([input_dir, output_dir]))

# run(input_dir, output_dir)