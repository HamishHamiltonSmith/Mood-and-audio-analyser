import numpy as np

def get_amp(file):
    from scipy.io.wavfile import read
    rate=4400
    _,data = read(str(file))
    duration = len(data)/rate
    N = rate*duration
    time = np.arange(0,duration,1/rate)
    x = time
    y = data
    idx = np.argmax(y)
    try:
        return str((x[idx]))
    except IndexError:
        return "Unable to calculate: index error"





def get_pitch(file):
    from aubio import source, pitch
    import sys
    win_s = 4096
    hop_s = 560 

    s = source(str(file), 44100, hop_s)
    rate = s.samplerate

    tolerance = 10

    pitch_o = pitch("yin", win_s, hop_s, rate)
    pitch_o.set_unit("midi")
    pitch_o.set_tolerance(tolerance)

    pitches = []
    confidences = []

    total_frames = 0
    while True:
        samples, read = s()
        pitch = pitch_o(samples)[0]
        pitches += [pitch]
        confidence = pitch_o.get_confidence()
        confidences += [confidence]
        if read < hop_s:
            break
    return(str(np.array(pitches).mean()+260))


def get_mood(file,gender,ageraw):
    age = int(ageraw)

    mood_key = {
        -3:"\nvery poor mood",
        -1:"\nquite poor mood",
        0:"\nneutral mood",
        1:"\nFairly good mood",
        3:"\nGreat mood!"

    }

    if gender == 1:
        gender = "male"
    elif gender == 2:
        gender = "female"
    freq = get_pitch(file)
    amp = get_amp(file)
    mood = 0
    if age >= 13:
        if gender == "Male":
            if float(freq) > 280:
                mood += 1
                if float(freq) > 300:
                    mood += 2
            elif float(freq) < 250:
                mood -= 1
                if float(freq) < 200:
                    mood -= 2

        elif gender == 'Female':
            if float(freq) > 330:
                mood += 1
                if float(freq) > 360:
                    mood += 2
            elif float(freq) < 300:
                mood -= 1
                if float(freq) < 280:
                    mood -= 2
    elif age < 13:
        if gender == "Male" or gender == "Female":
            if float(freq) > 340:
                mood += 1
                if float(freq) > 380:
                    mood += 2
            elif float(freq) < 280:
                mood -= 1
                if float(freq) < 250:
                    mood -= 2


    return str(mood) + " " + mood_key.get(mood) 