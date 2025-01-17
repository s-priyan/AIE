## **The swell knowledge work dataset for stress and user modelling research**
* Stress 
    1. Task load which poses demands on the worker
    2. mental effort which the worker needs to handle the task
    3. emotional response to a task
* Dataset characteristics 
    1. Recorded in real world office setting instead of artificial tasks.
    2. stressors should be manipulated in a systematic way.
    3. stressors should be assessed with validated questionnaires.
* This dataset overcomes 3 major drawbacks from existing datasets.
    1. Performs in natural office work.
    2. Used variety of sensors that can easily deployed in real world office settings instead of expensive/ obtrusive equipment
    3. Provides pre-processed and interpreted form of data with raw data.
* Features – computer interactions, video for facial expressions, Kinect 3D for body postures and body sensor for heart rate and ski conductance
# **Data collection**
1. Neutral – approx. 45 min
2. Stressor ‘time pressure’- max 30 min for a task
3. Stressor ‘Interruption’- 8 emails was sent during task

* Each of the experimental blocks started with a relaxation phase of about 8 mins. (Which is typical for stress research)
* To collect a ground truth of the subjective experience after each block, we used a combination of validated questionnaires.
    - Task load (mental demand, physical demand, temporal demand, effort, performance, and frustration) NASA-TLX
    - Mental effort Rating Scale Mental Effort
    - Emotion response (valence, arousal, and dominance) Self-Assessment Manikin Scale
    - Perceived stress on visual analogue scale from not stressed to very stressed (10-point scale)
    - Internal control index questionnaire
    - Rate their interest in topics - 7 point Likert scale(not interesting/difficult to very interesting/difficult)
# **Sensors**
* Computer logging – key logging application uLog
* Video 
    - face and upper body (USB camera placed below participant’s monitor). Then face reader to further analysis video data.
    - Additional webcam was placed above participant’s monitor.
* Kinect 3D 
    - body posture with Kinect 3D camera placed in front of participants at a distance about 2 meters to capture their whole body.
    - Also recorded RGB video.
* Body sensors 
    - ECG was recorded using a Mobi device(TMSI) with self-adhesive electrodes
    - Skin conductance was recorded using Mobi with finger electrodes.
* Additional lab recordings
    - lab’s ceiling camera and micro phones were used for making records of the lab during whole experiment. And screen capturing of participant’s screen.
# **Dataset**
1.	Feature data
    -	25 participant’s data.
    -	Contains pre-processed data, aggregated per minute.
    -	Contains following features
        - 12 computer interaction features
        - 40 facial expression features
        - 88 body posture features
        - 3 physiology features
    -	Provides the scores on questionnaire items as ground truth for the subjective experience in each condition
2.	Raw data and pre-processing

# **Analysis**

* Work stress 
1.	Stressor ‘time pressure’ – higher temporal demand, high arousal
2.	Stressor ‘email interruptions’ – more mental effort, more positive valence and more dominance
3.	Perceived stress – did not differ significantly between in the stressor and neutral conditions. Stress might be a too complex concept to measure in a short term work task.
* User modelling 
	- Mental effort might be estimated based on video information
    - Higher mental effort showed more activation in facial action units LidTighter, upper LipRaiser, Brow Lowerer and CheekRaiser
* Context recognition and information support 

**Reference**
[1] Saskia Koldijk, Maya Sappelli, Suzan Verberne, Mark A. Neerincx, and Wessel Kraaij. 2014. The SWELL Knowledge Work Dataset for Stress and User Modeling Research. In Proceedings of the 16th International Conference on Multimodal Interaction (ICMI '14). ACM, New York, NY, USA, 291-298
