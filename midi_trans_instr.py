from mido import MidiFile
from midiutil import MIDIFile
import music21 as m21
import glob
from music21 import converter,instrument
import sys
midi_sounds = {
 1 :	instrument.Piano(),
2:	"Bright Acoustic Piano",
3:	"Electric Grand Pian",
4:	"Honky-tonk Piano",
5 :	instrument.ElectricPiano(),
6:	instrument.ElectricPiano(),
7:	instrument.Harpsichord(),
8:	instrument.Clavichord(), #clavi??
9:	instrument.Celesta(),
10:	instrument.Glockenspiel(),
11:	"Music Box",
12:	 instrument.Vibraphone(),
13:	instrument.Marimba(),
14:	instrument.Xylophone(),
15 :instrument.TubularBells(),
16:	instrument.Dulcimer(),
17:	"Drawbar Organ",
18:	"Percussive Organ",
19:	"Rock Organ",
20:	"Church Organ",
21:	instrument.ReedOrgan(),
22:	instrument.Accordion(),
23: instrument.Harmonica(),
24:	"Tango Accordion",
25:	instrument.AcousticGuitar(),
26:	instrument.AcousticGuitar(),
27:	instrument.ElectricGuitar(),
28:	instrument.ElectricGuitar(),
29:	instrument.ElectricGuitar(),
30:	"Overdriven Guitar",
31:	"Distortion Guitar",
32:	"Guitar harmonics",
33:	instrument.AcousticBass(),
34:	instrument.ElectricBass(),
35:	instrument.ElectricBass(),
36:	"Fretless Bass",
37:	"Slap Bass 1",
38:	"Slap Bass 2",
39:	"Synth Bass 1",
40:	"Synth Bass 2",
41: instrument.Violin(),
42:	instrument.Viola(),
43:	"Cello",
44:	instrument.Contrabass(),
45:	"Tremolo Strings",
46:	"Pizzicato Strings",
47:	instrument.Harp(),
48:	instrument.Timpani(),
49:	"String Ensemble 1",
50:	"String Ensemble 2",
51:	"SynthStrings 1",
52:	"SynthStrings 2",
53:	"Choir Aahs",
54:	"Voice Oohs",
55:	"Synth Voice",
56:	"Orchestra Hit",
57:	instrument.Trumpet(),
58:	instrument.Trombone(),
59:	instrument.Tuba(),
60:	"Muted Trumpet",
61:	instrument.Horn(), #french???
62:	instrument.BrassInstrument(), #???
63:	"SynthBrass 1",
64:	"SynthBrass 2",
65:	instrument.SopranoSaxophone(),
66:	instrument.AltoSaxophone(),
67:	instrument.TenorSaxophone(),
68:	instrument.BaritoneSaxophone(),
69:	instrument.Oboe(),
70:	instrument.EnglishHorn(),
71:	instrument.Bassoon(),
72:	instrument.Clarinet(),
73:	"Piccolo",
74:	instrument.Flute(),
75:	instrument.Recorder(),
76:	instrument.PanFlute(),
77:	"Blown Bottle",
78:	instrument.Shakuhachi(),
79:	instrument.Whistle(),
80:	instrument.Ocarina(),

# 81:	Lead 1 (square)
# 82:	Lead 2 (sawtooth)
# 83:	Lead 3 (calliope)
# 84:	Lead 4 (chiff)
# 85:	Lead 5 (charang)
# 86:	Lead 6 (voice)
# 87:	Lead 7 (fifths)
# 88:	Lead 8 (bass + lead)
# 89:	Pad 1 (new age)
# 90:	Pad 2 (warm)
# 91:	Pad 3 (polysynth)
# 92.	Pad 4 (choir)
# 93.	Pad 5 (bowed)
# 94.	Pad 6 (metallic)
# 95.	Pad 7 (halo)
# 96.	Pad 8 (sweep)
# 97.	FX 1 (rain)
# 98.	FX 2 (soundtrack)
# 99.	FX 3 (crystal)
# 100.	FX 4 (atmosphere)
# 101.	FX 5 (brightness)
# 102.	FX 6 (goblins)
# 103.	FX 7 (echoes)
# 104.	FX 8 (sci-fi)
 105:	instrument.Sitar(),
106:	instrument.Banjo(),

 107:	instrument.Shamisen(),
 
 108:	instrument.Koto(),

 109:	 instrument.Kalimba(),
 
# 110.	Bag pipe
# 111.	Fiddle
112:	instrument.Shehnai(),
# 113.	Tinkle Bell
 114:	instrument.Agogo(),
 115: instrument.SteelDrum(),
 116: instrument.Woodblock(),
 117:	 instrument.Taiko(),
 118:	instrument.Timpani(),
# 119.	Synth Drum
# 120.	Reverse Cymbal
# 121.	Guitar Fret Noise
# 122.	Breath Noise
# 123.	Seashore
# 124.	Bird Tweet
# 125.	Telephone Ring
# 126.	Helicopter
# 127.	Applause
# 128.	Gunshot   
}
    
def main():
    input = 10110110
    input = (2 & 6)
    print(input)
    # fileHandler = Midis("./Sample.mid")
    
    
    
    fileHandler = FileHandler("./gotg_hol_intro.mid")
    nonTransposedMidi = fileHandler.GetSongFromDirectory()
    #nonTransposedMidi = fileHandler.GetSongFromDirectory()
    #print(nonProcessedMidi) prints a list of midi files

    transposer = Midis(nonTransposedMidi)
    transposer.AlterInstrument("./gotg_hol_intro.mid", 15)
    transposer.TransposeMidi("./ans.mid", 12)
   
    
    print("hello world")
    print(instrument.Piano())
  
  
        
        
        
        
    #transposer.TransposeMidi(2)
    
    
    # mid = MidiFile('Sample.mid', clip=True)
    # print(mid)
    # print(m21.pitch.Pitch('C'))   
    
    
        
    
class FileHandler:
    #Attributes
    songs = []
    #Constructor
    def __init__(self, filePath):
        self._filePath = filePath
    #Properties
    #Methods
    def GetSongFromDirectory(self):
        for i in glob.iglob(self._filePath + '/*.mid'):
            self.songs.append(i)
        return self.songs
    def CreateNewTransposedMidi():
        pass
    
json_types = [int, float, str, instrument]
string_to_type_dict = {t.__name__: t for t in json_types}

assert len(string_to_type_dict) == len(json_types)

def string_to_type(s):
    return string_to_type_dict[s]

def type_to_string(t):
    return t.__name__
    
class Midis:
    def __init__(self, filePath):
        self._filePath = filePath 
    
        
    
        
    def AlterInstrument(self, filePath, instrument):
        
        s = converter.parse(filePath)
        for el in s.recurse():
            if 'Instrument' in el.classes: # or 'Piano'
                
                el.activeSite.replace(el, midi_sounds[instrument])
        
        s.write('midi', "/Users/simoncooper/Desktop/kocree/ans.mid")
                
        
        

    
    
    
    
    
    
    def TransposeMidi(self, path, semis):
        print("hello")
        
        if not isinstance(semis, int):
            raise ValueError
        print("hi")
        midi_file = MidiFile(path, clip=True)
        
        
        
        for i, message in enumerate(midi_file.tracks[0]):
           
            
            
            
           
            
            
            if message.type in ('note_on','note_off'):
                message.note += semis
        for msg in midi_file:
            
            
            
            if msg.type == 'program_change':
                print(msg)
        
        midi_file.save("/Users/simoncooper/Desktop/kocree/trans.mid")
                
                    
        # 
        # for i in self._filePath:
        #     musicScorData = m21.converter.parse(i)
        #     key = musicScorData.analyze('key')
        #     print(key.mode)
        
        
        
        
if __name__=='__main__':
    main()
        