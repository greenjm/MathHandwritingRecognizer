import svmTrainer as trainer

#trainer.runSVMTrainPipeline("C:\Users\Josh\Downloads\extracted_images\extracted_images", 1, True, 9, 4)

#trainer.getClassifierAccuracy("C:\Users\Josh\Downloads\extracted_images\extracted_images", 1, 9)

trainer.getVotingAccuracy("C:\Users\Josh\Downloads\extracted_images\extracted_images", 5, 5)