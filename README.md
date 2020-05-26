
Line follower robot

Concept of Line Follower Robot:
Concept of line follower is related to light. Here the behaviour of light at black and white surface. When light fall on a white surface it will almost full reflects and in case of black surface light is absorbed by black surface.
  

Programming Explanation:
In program first of all we defines input and output pin. And then in main function we checks inputs and sends output according to inputs to output pin for driving motor. For checking input pin we used “if” statements.

There are four conditions in this line follower. We have used two sensor namely left sensor and right sensor.

Input                            	  Output	               Movement of Robot
Left Sensor	Right Sensor	Left Motor	 Right Motor
     LS	          RS	     LM1	 LM2	 RM1	  RM2	
0	                 0	      1	    0	     1	   0	              Forward
0	                 1	      1	    0	     0	   0	            Turn Right
1	                 0	      0	    0	     1	   0	             Turn Left
1	                 1	      0	    0	     0	   0	               Stop
 



 
