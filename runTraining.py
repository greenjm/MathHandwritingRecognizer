import svmTrainer as trainer

# Example filepath: "C:\Users\greenjm\Downloads\extracted_images\extracted_images"

"""
Use this line to train a classifier.
The first argument must be the absolute path
to the dataset. Then, the # of classifiers to train.
the third argument should always be true to use HOG.
Then, a fileID (all SVMs are named fileID + 'optimalCLF.pkl')
Lastly, an incrementor telling the trainer which portion of the
dataset to use (0 - 4)
"""
trainer.runSVMTrainPipeline("FILEPATH", 1, True, 0, 0)
trainer.runSVMTrainPipeline("FILEPATH", 1, True, 1, 1)
trainer.runSVMTrainPipeline("FILEPATH", 1, True, 2, 2)
trainer.runSVMTrainPipeline("FILEPATH", 1, True, 3, 3)
trainer.runSVMTrainPipeline("FILEPATH", 1, True, 4, 4)

"""
Get solo classifier accuracies. Give filepath to dataset,
the number of CLFs, and which file ID to start with.
"""
trainer.getClassifierAccuracy("FILEPATH", 5, 0)

"""
Get voting accuracy. Give filepath to dataset, number
of CLFs, and the file ID to start with. This can only work
if getAccuracies() in symbolDict.py contains the accuracies
found from the getClassifierAccuracy() function.
"""
trainer.getVotingAccuracy("FILEPATH", 5, 0)