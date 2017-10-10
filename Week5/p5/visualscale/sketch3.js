
var serial;         // variable to hold an instance of the serialport library
var portName = '/dev/cu.usbmodem1411';  // fill in your serial port name here
var potentiometer;
var people;
var difficulty;
var weight;
var le = 0;
var weightPage = 0.03;
var minPerSent = 0;
var minPerPage = 0;
var coverWeightPaper = 0.15;
var numWord = 0;
var totalWeight = 0;
var numPages = 0;
var timeReadingMinutes = 0;
var timeReadingHours = 0;
var readingDifficulty = 0;
var finalTime = 0;
var finalTimeDec = 0;


function setup(){
	
	serial = new p5.SerialPort();
	serial.on('data', serialEvent); 
	createCanvas(1400, 800);	

}




function draw(){

	//graphic frame 
	background(100);
	stroke(255);
	line(800, 0, 800, 1200);
	line(800, 350, 1700, 350);
	leftBackground();

	//weight graphic
	weightGraphic();
	//figure drawing
	fill(255);
	ellipse(400, 330 - le, 100, 100);
	fill(255);
	rect(395,370 - le, 10, 20);
	fill(255);
	rect(380, 390 - le, 40, 100);
	stroke(255);
	fill(255);
	line(395, 490 - le, 395, 550);
	stroke(255);
	fill(255);
	line(405, 450 - le, 405, 550);

	// People status
		noStroke();
		fill(255);
		textSize(14);
		text("Are you an adult?", 850, 40);
	if (people <= 1){
		fill(255);
		textSize(26);
		text("Duh. I'm an adult!", 850, 80);
		le = 100;
		}
	else { 
		fill(255);
		textSize(26);
		text("No, I am a kid!", 850, 80);
		le = 10;
		}

	// Difficulty status
	fill(255);
	textSize(14);
	text("How difficult is this book?", 850, 130);
	if (difficulty <= 1){
		fill(255);
		textSize(26);
		text("This is an advanced read for me.", 850, 170);}
	else{
		fill(255);
		textSize(26);
		text("Just a normal read for me.", 850, 170);
	}

	// Pot status
	fill(255);
	textSize(14);
	text("Open a page. Tell me how many words are there in one line?", 850, 220);
	if (potentiometer <= 85){
		fill(255);
		textSize(26);
		text("0 - 6 words", 850, 260);}
	else if(potentiometer >=86 && potentiometer <=170){
		fill(255);
		textSize(26);
		text("7 - 12 words", 850, 260);}
	else if (potentiometer >=171) {
		fill(255);
		textSize(26);
		text("more than 12 words", 850, 260);
	}
	fill(255);
	rect(850, 280, 20 + potentiometer * 1.3, 40);
	

	// Final Result Graphics
	fill(200);
	textSize(14);
	text("This book will take you", 850, 380);
	fill(255);
	textSize(90);
	text(finalTimeDec, 850, 470);
	fill(200);
	textSize(14);
	text("hours to read.", 1050, 470);



	//Algorithm monitor 
	fill(255);
	textSize(12);
	text("people read: " + people, 850, 750);
	fill(255);
	textSize(12);
	text("potentiometer read: " + potentiometer, 850, 770);
	fill(255);
	textSize(12);
	text("difficulty read: " + difficulty, 1100, 750);
	fill(255);
	textSize(12);
	text("weightsensor read: " + weight, 1100, 770);

	potReading();
	readDifficulty();
	timeReading();
	kidLock();


} // draw ends here



	function potReading() {
	if (potentiometer <= 85){
		numWord = 6;
	}
	else if (potentiometer >= 86 && potentiometer <= 170){
		numWord = 12;
	}
	else if (potentiometer >= 171){
		numWord = 15;
	}
}

	function readDifficulty(){
		if (people < 1 && difficulty < 1){
			readingDifficulty = 1.4;
		}
		else if (people < 1 && difficulty > 1){
			readingDifficulty = 1;
		}
		else if (people > 1 && difficulty < 1){
			readingDifficulty = 5;
		}
		else if (people > 1 && difficulty > 1){
			readingDifficulty = 1.4;
		}
	}

	function timeReading(){
		minPerSent = numWord / 200;
		console.log("minsPerSent");

		minPerPage = minPerSent * 35;
		totalWeight = weight - coverWeightPaper;
		numPages = totalWeight / weightPage;
		timeReadingMinutes = numPages * minPerPage;
		timeReadingHours = timeReadingMinutes / 60;
		finalTime = timeReadingHours * readingDifficulty;
		finalTimeDec = finalTime.toFixed(2);
		if (finalTimeDec < 0){
			finalTimeDec = 0;
		}
		console.log("timeReading");
	}

	function kidLock(){
		if (people > 1 && difficulty < 1){
			fill(0, 0, 0, 220);
			rect(800, 0, 800, 1000);
			textSize(20);
			text("Go outside child, enjoy the sun!", 250, 100);
		}
	} 

	function leftBackground(){
		if (people > 1 && difficulty < 1){
			fill(141, 213, 232);
			rect(0, 0, 800, 800);
		}
		else {
			fill(30);
			noStroke();
			rect(0,0, 800, 800);

		}
	}

	function weightGraphic(){
		if (people > 1 && difficulty < 1){
			noStroke();
			fill(244, 205, 48);
			ellipse(400, 400, 100 + weight * 100, 100 + weight * 100);}
		else {
			noStroke();
			fill(100, 20, 10, 200);
			ellipse(400, 400, 100 + weight * 100, 100 + weight * 100);}

	}


function serialEvent(){
	//inData = Number(serial.read());
    var inString = serial.readStringUntil('\r\n');
    //println("raw: \t" + inString); // <- uncomment this to debug serial input from Arduino

    if (inString != null) {
      // trim off any whitespace:
      inString = trim(inString);

    	if (inString.length > 3) {
    		var values = split(inString, ',');

    			potentiometer = values[0];
    			people = values[1];		
    			difficulty = values[2];
    			weight = values[3];
  		}
	}	
}









