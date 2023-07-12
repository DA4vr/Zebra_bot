import random
from discord.ext import commands
from typing import Any, Tuple, List
########################### LISTS
phasmophobia = ["flashlight", "camera", "video camera", "sound sensor", "crucifix", "smudge stick", "uv light",
                "emf reader", "ghost writing book", "crucifix", "candle", "spirit box", "dots projector"]
dead_by_daylight = ["Dwight Farfield", "Meg Thomas", "Claudette Morel", "Jake Park", "Bill Overbeck", "Nea Karlsson",
                    "Ace Viscotti", "Feng Min", "David King", "Kate Denson", "Adam Francis", "Jeff Johansen",
                    "Ashley Williams", "Nancy Wheeler", "Steve Harrington", "Yui Kimura", "Cheryl Mason",
                    "Felix Ritcher",
                    "Jill Valentine", "Leon Kennedy", "Mikaela Reid", "Vittorio Toscano", "Haddie Kaur",
                    "Jonah Vasquez"]
dead_by_daylight_SurvivorPerks = ["Ace in the hole", "Adrenaline", "Aftercare", "Alert", "Any means neccessary",
                                  "Appraisal",
                                  "Autodidact", "Background Player", "Balanced Landing", "Better Than New",
                                  "Bite The Bullet",
                                  "Blast Mine", "Blood Pact", "Blood Rush", "Boil Over", "Bond",
                                  "Boon:Circle of Healing",
                                  "Boon:Dark Theory", "Boon:Exponential", "Boon:Shadow Step", "Borrowed Time",
                                  "Botany Knowledge", "Breakdown", "Buckle Up", "Built To Last", "Calm Spirit",
                                  "Clairvoyance",
                                  "Corrective Action", "Counterforce", "Cut Loose", "Dance with me", "Dark sense",
                                  "Dead Hard",
                                  "Deception", "Decisive Strike", "Deliverance", "Desperate Measure",
                                  "Detectives Hunch",
                                  "Distortion", "Diversion", "Déjà Vu", "Empathic Connection", "Fast Track",
                                  "Flashbang", "Flip-Flop",
                                  "Fogwise", "For the People", "Friendly Competition", "Guardian", "Head on", "Hope",
                                  "Hyperfocus", "Inner Healing", "Iron Will", "Kindred", "Kinship", "Leader",
                                  "Left Behind", "Lightweight",
                                  "Lithe", "Low Profile", "Lucky Break", "Made For This", "Mettle of Man", "No Mither",
                                  "No One Left Behind", "Object of Obsession", "Off the Record", "Open-Handed",
                                  "Overcome",
                                  "Overzealous", "Parental Guidance", "Pharmacy", "Plunderer's Instinct", "Poised",
                                  "Potential Energy"
                                  "Power Struggle", "Premonition", "Prove Thyself", "Quick and Quiet", "Quick Gambit",
                                  "Reactive Healing",
                                  "Reassurance", "Red Herring", "Renewal", "Repressed Alliance", "Residual Manifest",
                                  "Resilience",
                                  "Rookie Spirit", "Saboteur", "Scavenger", "Self-Aware", "Self-care",
                                  "Self Preservation", "Situational Awareness",
                                  "Slippery Meat", "Small Game", "Smash Hit", "Sole Survivor",
                                  "Solidarity", "Soul Guard", "Spine Chill",
                                  "Sprint Burst", "Stake Out", "Streetwise", "Teamwork: Collective Stealth",
                                  "Teamwork: Power of Two",
                                  "Technician", "Tenacity", "This Is Not Happening", "Troubleshooter", "Unbreakable",
                                  "Up the Ante",
                                  "Urban Evasion", "Vigil", "Visionary", "Wake Up!", "We'll Make It",
                                  "We're Gonna Live Forever",
                                  "Wiretap", "Windows of Opportunity"]
MW2_callofduty_primaryGuns = ["M4", "TAQ-56", "KASTOV 762", "LACHMANN-556", "STB 55G", "M16", "KASTOV-74U",
                              "KASTOV 545",
                              "CHIMERA",
                              "M13B", "ISO HEMLOCK", "TEMPUS RAZORBACK", "LACHMANN-761", "SO-14", "TAQ-V",
                              "FTAC RECON",
                              "CRONEN SQUALL",
                              "TEMPUS TORRENT", "VEL 46", "MX9", "LACHMANN SUB", "VAZNEV-9K", "FSS HURRICANE",
                              "MINIBAK",
                              "PDSW 528",
                              "FENNEC 45", "ISO 45", "SAKIN MG38", "HCR 56", "556 ICARUS", "RAAL MG", "RPK", "RAPP H",
                              "EBR-14",
                              "SP-R 208",
                              "LOCKWOOD MK2", "LM-S", "SA-B 50", "TAQ-M", "LOCKWOOD 300", "EXPEDITE 12", "BRYSON 800",
                              "BRYSON 890", "KV BROADSIDE",
                              "MCPR-300", "SIGNAL 50", "LA-B 330", "SP-X 80", "FJX IMPERIUM"]
MW2_callofduty_secondaryGuns = ["RIOT SHIELD", "COMBAT KNIFE", "P890", ".50 GS", "X12", "Basilisk ", "X13 Auto",
                                "FTAC SIEGE",
                                "GS MAGNA", "PILA", "STRELA-P", "JOKR", "RPG-7"]
MW2_callofduty_Lethals = ["C4", "CLAYMORE", "DRILL CHARGE", "FRAG", "SENTEX", "MOLOTOV", "PROXIMITY MINE", "THERMITE",
                          "THROWING KNIFE"]
MW2_callofduty_Tactical = ["DECOY", "FLASH", "GAS", "HEARTBEAT SENSOR", "SHOCK STICK", "SPOTTER SCOPE", "SMOKE",
                           "STIM", "STUN"]
########################### randomization process with no duplication.
def get_randomizedPhasmo():
    randomized_phasmo = random.sample(phasmophobia, 3)
    return randomized_phasmo
def get_randomizedDeadbyDaylightPerks():
    randomized_DeadbyDaylightPerks = random.sample(dead_by_daylight_SurvivorPerks, 4)
    return randomized_DeadbyDaylightPerks
def get_randomizedPrimaryGuns():
    randomizedPrimaryGuns = random.sample(MW2_callofduty_primaryGuns, 2)
    return randomizedPrimaryGuns
def is_user_author(author_id):
    def check(message):
        return message.author.id == author_id

    return check

def case_14 (message):
    if message == 'zebra randomizeloadout2p' :
        return (get_randomizedPrimaryGuns(), random.choice(MW2_callofduty_Lethals),
                random.choice(MW2_callofduty_Tactical))
def case_1 (message):
    if message == 'zebra randomizeloadout2p' :
        return (get_randomizedPrimaryGuns(), random.choice(MW2_callofduty_Lethals),
                random.choice(MW2_callofduty_Tactical))
def case_2(message):
    if message == 'zebra randomizeloadout1p1s':
        return (random.choice(MW2_callofduty_primaryGuns), random.choice(MW2_callofduty_secondaryGuns),
                random.choice(MW2_callofduty_Lethals),
                random.choice(MW2_callofduty_Tactical))
def case_3(p_message):
    if p_message in ['hello zebra', 'zebra hello', 'hi zebra', 'zebra hi', 'hey zebra', 'zebra hey']:
        return "Hello! how can i assist you today?"
def case_4 (message):
    if message == 'zebra roll' or message == 'roll zebra' :
        try:
            #input1 prompts the user to enter 2 integers
            input1 = input("Select two values to roll from (e.g., 0, 6): ")
            #val.strip() = removing any trailing whitespace
            #input1.split(',') : splits variables using ','
            #int(val.string[) applied to each stripped substring (substring that removed whitespace
            # and convert string to integer to insure entry of integers.
            #input2 stores the first integer in index 0 and second integer in index1
            input2 = [int(val.strip()) for val in input1.split(',')]
            finalizedRoll = str(random.randint(input2[0],input2[1]))
        except ValueError:
            print("Please enter numbers")
        return finalizedRoll
def case_5 (p_message):

    if p_message == 'zebra help' or p_message == 'help zebra':
        return '`zebra hello ~~ greeting`\n' \
               '`zebra roll ~~ roll a number between 1 and 7`\n' \
               '`zebra randphasmo ~~ randomize 3 phasmophobia items`\n' \
               '`zebra randsurvivor ~~ randomize dbd survivor`\n' \
               '`zebra randomizeSPerks ~~ randomize survivor perks\n`' \
               '`zebra randomizeloadout2p ~~ randomize loadout with 2 primary guns on MW2`\n' \
               '`zebra randomizeloadout1p1s ~~ randomize loadout with 1 primary gun and a secondary on MW2\n`'
def case_6 (message):
    if message == 'zebra randphasmo':
        return get_randomizedPhasmo()
def case_7(message):
    if message == 'zebra randsurvivor':
        return random.choice(dead_by_daylight)
def case_8(message):
    if message == 'zebra randomizeSPerks':
        return get_randomizedDeadbyDaylightPerks()


def get_response(message) -> str | tuple[Any, Any, list[str], list[str]] | Any:
    # tuple[Any, Any, list[str], list[str]] | Any:
    global answer
    p_message = message.lower()

    if p_message == 'hello zebra' or p_message == 'zebra hello' or p_message == 'hi zebra' or p_message == 'zebra hi' or \
            p_message == 'hey zebra' or p_message == 'zebra hey':
        # can be written as if p_message in [".............."] return
        return 'Hello there!'

    if message == 'zebra roll':
        try:
            input1 = input("Select two values to roll from (e.g., 0, 6): ")
            input2 = [int(val.strip()) for val in input1.split(',')]
            finalizedRoll = str(random.randint(input2[0], input2[1]))
        except ValueError:
            print("Please enter numbers")
        return finalizedRoll

    if p_message == 'zebra help' or p_message == 'help zebra':
        return '`zebra hello ~~ greeting`\n' \
               '`zebra roll ~~ roll a number between 1 and 7`\n' \
               '`zebra randphasmo ~~ randomize 3 phasmophobia items`\n' \
               '`zebra randsurvivor ~~ randomize dbd survivor`\n' \
               '`zebra randomizeSPerks ~~ randomize survivor perks\n`' \
               '`zebra randomizeloadout2p ~~ randomize loadout with 2 primary guns on MW2`\n' \
               '`zebra randomizeloadout1p1s ~~ randomize loadout with 1 primary gun and a secondary on MW2\n`'

    if message == 'zebra randphasmo':
        return get_randomizedPhasmo()

    if message == 'zebra randsurvivor':
        return random.choice(dead_by_daylight)

    if message == 'zebra randomizeSPerks':
        return get_randomizedDeadbyDaylightPerks()

    if message == 'zebra randomizeloadout2p':
        return (get_randomizedPrimaryGuns(), random.choice(MW2_callofduty_Lethals),
                random.choice(MW2_callofduty_Tactical))
    if message == 'zebra randomizeloadout1p1s':
        return (random.choice(MW2_callofduty_primaryGuns),random.choice(MW2_callofduty_secondaryGuns),
                random.choice(MW2_callofduty_Lethals), random.choice(MW2_callofduty_Tactical))


