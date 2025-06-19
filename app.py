from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Voice Leasing Agent is running."

@app.route("/voice", methods=["POST"])
def voice():
    resp = VoiceResponse()
    gather = Gather(input="speech", action="/handle", speechTimeout="auto", timeout=5)
    gather.say("Thanks for calling Calgary Apartments. This is Abe speaking, How can I help you today?", voice="Polly.Matthew-Neural")
    resp.append(gather)
    return Response(str(resp), mimetype="application/xml")

@app.route("/handle", methods=["POST"])
def handle():
    user_input = request.values.get("SpeechResult", "").lower()
    resp = VoiceResponse()

    if "book" in user_input or "tour" in user_input:
        resp.say("Sure, I can help with that. In the full version, I would now offer real-time tour availability.", voice="Polly.Matthew-Neural")

    elif "pet" in user_input:
        resp.say("Yes, we are pet-friendly. Small dogs and cats are welcome with a deposit.", voice="Polly.Matthew-Neural")

    elif "gym" in user_input or "fitness" in user_input:
        resp.say("Our fitness center is open 24/7 for all residents.", voice="Polly.Matthew-Neural")

    elif "parking" in user_input:
        resp.say("We offer heated underground parking for fifty dollars a month.", voice="Polly.Matthew-Neural")

    elif "pool" in user_input:
        resp.say("Yes, we have an indoor saltwater pool open from 6 AM to 10 PM daily.", voice="Polly.Matthew-Neural")

    elif "floor plan" in user_input or "units" in user_input or "types" in user_input:
        resp.say("We offer studio, one-bedroom, and two-bedroom units. Visit calgaryapartments.ca for floorplans.", voice="Polly.Matthew-Neural")

    else:
        resp.say("This is a demo version. In production, I’d respond with more leasing info and even schedule your tour.", voice="Polly.Matthew-Neural")

    resp.hangup()
    return Response(str(resp), mimetype="application/xml")

if __name__ == "__main__":
    app.run()
