## Approaches

#### Posture Assessment 

```
> Method I:
Extract skeleton points (calculate angle), feed that angles/skeleton points to a sequential model(RNN/LSTM) to extract temporal features and give the prediction as bad posture, good posture, prolonging static posture. (DISSCUSSED)
	- Long time training is required
	- More dataset are needed
	- High manual annotation needed
	- Validation method is unknown or in confusion

> Method II:	
Extract skeleton points, Extract the angles needed to calculate the RULA/REBA score which indicates whether the posture is good or bad. A sequential model(RNN/LSTM) which takes angles/ changes in angles as input and output whether the posture changed or not as output. This information along with RULA/REBA score can be used to classify the postures as good, bad and prolonging static posture. (DISCUSSION NEEDED)
	- May not require long time training 
	- Less dataset in enough
	- Further study needed on RULA/REBA scoring methods
	- Need to make an algorithm on posture changes
	- May not need a strong validation as RULA/REBA provides strong validation itself.

> Method III: Good or Bad posture classification using a simple CNN on the images consists 2D-skeleton 

Step1- Select a bettter 2D-skeleton algorithm and apply  on frames/ images
Step2- Draw the 2D-skeleton on a black frame & label them as good or bad
Step3- CNN model building from the processed data
Step4- Testing from in real time and predict the accuracy using a confusion matrix
Step5- Tune the model and dataset and testing in a repeat manner

PROS: Faster than other methods, Low complexity, Camera position doesnot affect output
CONS: Low accurate (2D is weaker than 3D), prolonging static posture will be missed, have not found strong validation from the citations

Issue: How to make this method to temporal(Analysis on sequence of frames)
```

