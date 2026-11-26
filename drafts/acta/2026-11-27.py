# Ex Ōre Equī · Deutsch · Freitag 27 November 2026. FIRST GERMAN EPISODE. Free voices (Jenny + Thorsten). English → German on every line, then all the German again.
# Level: week 1 = A1 (main clauses, present tense; past only war/hatte). Grammar of the day (Friday): the future with werden.
# Sources (read 27 Nov 2026, early morning, Canberra): Bureau of Meteorology place pages (Canberra Central MS25, Mascot, South Melbourne, Kedron,
# North Perth, Novar Gardens, West Hobart, Berrimah) · Reuters via Devdiscourse, Business Upturn, ABC, AAP/Yahoo 26 Nov (gas bill) ·
# ABC, The Nightly 26 Nov (Leah Blyth) · ABC business blog, Savings.com.au 25 Nov, Broker Daily 26 Nov (CPI, RBA) ·
# ABC Australia 27 Nov, i24NEWS, Times of Israel/AFP 26 Nov, Reuters via BOE Report and RTÉ 26 Nov, CBS 25 Nov, Dawn, Anadolu 26 Nov (Iran, Kuwait) ·
# Ukrainian Air Force via Interfax-Ukraine, Euronews, AP, Spotmedia, Kyiv Post, Kyiv Independent 26 Nov (Ukraine) ·
# ABC News (ABC Great Southern) 26 Nov (Grinch, Kulin) · KSAT San Antonio 26 Nov (Raul Jimenez Thanksgiving Dinner).
import json, re
L = []
def en(t): L.append(['en', t])
def p1(t): L.append(['p1', t])
def pl(e, t): L.append(['pl', e, t])
def spl(e, t): L.append(['spl', e, t])
def p1pl(e, t): L.append(['p1pl', e, t])

# ---------------- opening ----------------
spl("Hello, listeners. This is the news, straight from the horse's mouth.", "Hallo, liebe Hörer. Hier sind die Nachrichten, direkt vom Pferd.")
pl("Today is Friday, the twenty-seventh of November, 2026.", "Heute ist Freitag, der siebenundzwanzigste November zweitausendsechsundzwanzig.")
pl("From today the news is in German. Every line in English, then in German.", "Ab heute sind die Nachrichten auf Deutsch. Jeder Satz auf Englisch, dann auf Deutsch.")
pl("First the weather. Then Australia. Then the world: Iran and Ukraine.", "Zuerst das Wetter. Dann Australien. Dann die Welt: der Iran und die Ukraine.")
pl("Then a good piece of news, the grammar of the day, and the words of the day.", "Dann eine gute Nachricht, die Grammatik des Tages und die Wörter des Tages.")

# ---------------- weather ----------------
en("The weather. Canberra today: 15 to 28, cloudy, showers most likely in the afternoon and evening, 60%, a thunderstorm possible, light winds. Saturday: 16 to 25, showers 95%, 15 to 45 mm, storms possible.")
spl("The weather.", "Das Wetter.")
pl("Today in Canberra it is cloudy. The wind is calm.", "Heute ist es in Canberra bewölkt. Der Wind ist ruhig.")
pl("In the morning fifteen degrees, in the afternoon twenty-eight degrees.", "Am Morgen fünfzehn Grad, am Nachmittag achtundzwanzig Grad.")
pl("In the late morning it is perhaps still dry. In the afternoon and in the evening: showers, sixty per cent, perhaps a thunderstorm.", "Am Vormittag ist es vielleicht noch trocken. Am Nachmittag und am Abend: Schauer, sechzig Prozent, vielleicht ein Gewitter.")
pl("Tomorrow, Saturday: sixteen to twenty-five degrees, and a lot of rain.", "Morgen, am Samstag: sechzehn bis fünfundzwanzig Grad und viel Regen.")
pl("The rain falls on the head and on the back. Good for the grass. The grass says thank you. Very quietly. Grass is very polite.", "Der Regen fällt auf den Kopf und auf den Rücken. Gut für das Gras. Das Gras sagt danke. Ganz leise. Gras ist sehr höflich.")
pl("In Sydney it is partly cloudy. Twenty-seven degrees.", "In Sydney ist es teilweise bewölkt. Siebenundzwanzig Grad.")
pl("In Melbourne a lot of rain and perhaps a thunderstorm. Twenty-five degrees. Today, do not wait long at the stop!", "In Melbourne viel Regen und vielleicht ein Gewitter. Fünfundzwanzig Grad. Heute nicht lange an der Haltestelle warten!")
pl("In Brisbane showers, twenty-nine degrees. In Perth it is calm and sunny, twenty-seven degrees.", "In Brisbane Schauer, neunundzwanzig Grad. In Perth ist es ruhig und sonnig, siebenundzwanzig Grad.")
pl("In Adelaide twenty-eight degrees, in Hobart twenty-six, in Darwin thirty-five degrees and showers.", "In Adelaide achtundzwanzig Grad, in Hobart sechsundzwanzig, in Darwin fünfunddreißig Grad und Schauer.")

# ---------------- Australia ----------------
en("Australia. South Australian Liberal senator Leah Blyth, a member of the shadow ministry, has defected to One Nation. October CPI 4.9%; electricity +25%, rents +3.5%; the RBA decides on 8 December at 2:30 pm. The gas reserve bill: the final vote is put off to February; the Coalition will not oppose it.")
spl("Australia.", "Australien.")
pl("Leah Blyth changes over, like on a train. She leaves the Liberals and goes to One Nation.", "Leah Blyth steigt um, wie im Zug. Sie verlässt die Liberalen und geht zu One Nation.")
pl("She turns her back on the Liberals.", "Sie kehrt den Liberalen den Rücken.")
pl("She is a senator from South Australia. New party, new address.", "Sie ist Senatorin aus Südaustralien. Neue Partei, neue Adresse.")
pl("She says: I can no longer in good conscience say: the Liberals can save this country.", "Sie sagt: Ich kann nicht mehr mit gutem Gewissen sagen: Die Liberalen können dieses Land retten.")
pl("Angus Taylor is the leader of the Liberals. He says: that is disappointing.", "Angus Taylor ist der Chef von den Liberalen. Er sagt: Das ist enttäuschend.")
pl("Tony Abbott says: that has nothing to do with principles. Nothing whatsoever.", "Tony Abbott sagt: Das hat nichts mit Prinzipien zu tun. Gar nichts.")
pl("Easy, easy, Canberra.", "Ruhig, ruhig, Canberra.")
pl("At the racetrack a jockey stays on the back of his horse. He does not change over in the middle of the race. In Canberra, apparently he does.", "Auf der Rennbahn bleibt ein Jockey auf dem Rücken von seinem Pferd. Er steigt nicht mitten im Rennen um. In Canberra offenbar schon.")
pl("Anthony Albanese says about Taylor: he wants to run the country, but he cannot even run his own team.", "Anthony Albanese sagt über Taylor: Er will das Land führen, aber er kann nicht einmal sein eigenes Team führen.")
pl("Yesterday: inflation is at four point nine per cent. Electricity costs twenty-five per cent more in one year, the rent three point five per cent more.", "Gestern: Die Inflation liegt bei vier Komma neun Prozent. Strom kostet in einem Jahr fünfundzwanzig Prozent mehr, die Miete drei Komma fünf Prozent mehr.")
pl("The customers get high bills for electricity. And the rent goes up too.", "Die Kunden bekommen hohe Rechnungen für Strom. Und die Miete steigt auch.")
pl("And oats? Not cheap either. Oats on special offer? Only in a dream.", "Und der Hafer? Auch nicht günstig. Hafer im Angebot? Nur im Traum.")
pl("The central bank decides on the eighth of December, at half past two in the afternoon.", "Die Zentralbank entscheidet am achten Dezember, um halb drei am Nachmittag.")
pl("Now the gas. The law for gas is still not finished. The last vote comes only in February.", "Jetzt das Gas. Das Gesetz für Gas ist noch nicht fertig. Die letzte Abstimmung kommt erst im Februar.")
pl("The Coalition says: we are not against it, for we want cheap gas.", "Die Koalition sagt: Wir sind nicht dagegen, denn wir wollen günstiges Gas.")
pl("Tim Ayres, the minister, says: the law brings cheap gas for firms and for households.", "Tim Ayres, der Minister, sagt: Das Gesetz bringt günstiges Gas für Firmen und für Haushalte.")
pl("Now parliament is empty. The law waits until February.", "Jetzt ist das Parlament leer. Das Gesetz wartet bis Februar.")
pl("Once more: Leah Blyth changes over, and the law for gas is still not finished.", "Noch einmal: Leah Blyth steigt um, und das Gesetz für Gas ist noch nicht fertig.")

# ---------------- Iran ----------------
en("Iran. On Thursday drones hit an air-defence station in Kuwait. Two Italian technicians were killed; a Pakistani and a Kuwaiti army captain were hurt. Kuwait: 'heinous Iranian aggression'. Iran denies it. The IRGC claims two tankers hit mines (unverified). Bessent: Iran has no oil on the water left to sell. Qatar and Pakistan pass proposals back and forth. Brent about $94.")
spl("The world. First, Iran.", "Die Welt. Zuerst der Iran.")
pl("Yesterday: Trump says: we can end the war at any time. Now: two dead in Kuwait.", "Gestern: Trump sagt: Wir können den Krieg jederzeit beenden. Jetzt: zwei Tote in Kuwait.")
pl("Drones hit a station for air defence in Kuwait. An important place.", "Drohnen treffen eine Station für die Luftabwehr in Kuwait. Ein wichtiger Ort.")
pl("Two technicians from Italy die. Two people are injured: a man from Pakistan and an officer from Kuwait.", "Zwei Techniker aus Italien sterben. Zwei Menschen sind verletzt: ein Mann aus Pakistan und ein Offizier aus Kuwait.")
pl("Kuwait says: that is a heinous Iranian aggression.", "Kuwait sagt: Das ist eine schlimme iranische Aggression.")
pl("Iran says: it was not us.", "Der Iran sagt: Wir waren es nicht.")
pl("We call Tehran. The line is engaged. Of course.", "Wir rufen in Teheran an. Die Leitung ist besetzt. Natürlich.")
pl("The Revolutionary Guard says: two tankers run onto mines. That is not confirmed. The crews are safe.", "Die Revolutionsgarde sagt: Zwei Tanker laufen auf Minen. Das ist nicht bestätigt. Die Mannschaften sind sicher.")
pl("Scott Bessent, the American finance minister, says: Iran has not a drop of oil left on the sea. Since August Iran's tankers have stayed empty.", "Scott Bessent, der amerikanische Finanzminister, sagt: Der Iran hat keinen Tropfen Öl mehr auf dem Meer. Seit August bleiben die Tanker vom Iran leer.")
pl("Qatar and Pakistan carry offers back and forth. But there is no solution yet.", "Katar und Pakistan bringen Angebote hin und her. Aber eine Lösung gibt es noch nicht.")
pl("A barrel of Brent oil costs about ninety-four dollars. For oil countries that is good business.", "Ein Barrel Brent-Öl kostet etwa vierundneunzig Dollar. Für Ölländer ist das ein gutes Geschäft.")
pl("A horse needs no petrol. It would like only oats. Oats are the solution for everything.", "Ein Pferd braucht kein Benzin. Es möchte nur Hafer. Hafer ist die Lösung für alles.")
pl("Once more: in Kuwait two Italians die, and Iran says: it was not us.", "Noch einmal: In Kuwait sterben zwei Italiener, und der Iran sagt: Wir waren es nicht.")

# ---------------- Ukraine ----------------
en("Ukraine. On the night to Thursday Russia launched 113 drones and ballistic missiles; 87 drones were shot down or jammed; hits at 20 locations. Kharkiv: 3 killed. Kyiv: a shopping centre hit. Trump: 'A COMPLETE BLOODBATH'; he would like to see Putin pull back. Kushner: Putin 'a grandmaster of politics'; the POW swap 'very soon, before the holidays', the biggest of the war.")
spl("Now Ukraine.", "Jetzt die Ukraine.")
pl("Yesterday: Zelensky is waiting for a date. Today: still no date, and attacks again.", "Gestern: Selenskyj wartet auf einen Termin. Heute: noch kein Termin, und wieder Angriffe.")
pl("In the night Russia sends one hundred and thirteen drones, and missiles as well. Ukraine stops eighty-seven drones.", "In der Nacht schickt Russland hundertdreizehn Drohnen, und dazu Raketen. Die Ukraine stoppt siebenundachtzig Drohnen.")
pl("The attacks hit twenty places. In Kharkiv three people die.", "Die Angriffe treffen zwanzig Orte. In Charkiw sterben drei Menschen.")
pl("In Kyiv a missile hits a shopping centre: a building with many shops.", "In Kiew trifft eine Rakete ein Einkaufszentrum: ein Haus mit vielen Geschäften.")
pl("Donald Trump writes: the war is a complete bloodbath. He also writes: Putin should stop all attacks in Europe.", "Donald Trump schreibt: Der Krieg ist ein totales Blutbad. Er schreibt auch: Putin soll alle Angriffe in Europa stoppen.")
pl("Jared Kushner says: Putin is a grandmaster in politics.", "Jared Kushner sagt: Putin ist ein Großmeister in der Politik.")
pl("In chess the horse jumps. Always like an L. Why? Nobody knows. Not even the horse.", "Im Schach springt das Pferd. Immer wie ein L. Warum? Das weiß niemand. Auch das Pferd nicht.")
pl("Kushner also says: the exchange of prisoners comes very soon, before the holidays. It is the biggest exchange in the whole war.", "Kushner sagt auch: Der Austausch von Gefangenen kommt sehr bald, noch vor den Feiertagen. Das ist der größte Austausch im ganzen Krieg.")
pl("Once more: one hundred and thirteen drones, three dead in Kharkiv, and the exchange comes soon.", "Noch einmal: hundertdreizehn Drohnen, drei Tote in Charkiw, und der Austausch kommt bald.")

# ---------------- good news ----------------
en("Good news. Kulin, Western Australia, about 282 km from Perth. In October an Italian tourist died in a crash near Kulin. Sergeant David Worcester found her service dog, Grinch, beside her and took him home. A vet more than 100 km away found two pelvic fractures; Worcester slept on the floor beside him and paid the vet bills himself. The owner's family flew from Italy; Grinch knew them at once. He flies home on 2 December (ABC News). And in San Antonio, Texas: the Raul Jimenez Thanksgiving Dinner for 25,000 people, every year since 1979, with free VIA buses for registered guests (KSAT).")
spl("And now, a good piece of news. It begins sadly, but it ends happily.", "Und jetzt eine gute Nachricht. Sie beginnt traurig, aber sie endet glücklich.")
pl("Kulin is a small place in Western Australia, far away from Perth: about two hundred and eighty-two kilometres.", "Kulin ist ein kleiner Ort in Westaustralien, weit weg von Perth: etwa zweihundertzweiundachtzig Kilometer.")
pl("In October a tourist from Italy had an accident near Kulin. The woman was dead.", "Im Oktober hatte eine Touristin aus Italien bei Kulin einen Unfall. Die Frau war tot.")
pl("Her dog Grinch lies next to her. Sergeant David Worcester, from the police, finds him.", "Ihr Hund Grinch liegt neben ihr. Sergeant David Worcester von der Polizei findet ihn.")
pl("He takes Grinch home. The vet is far away, more than a hundred kilometres.", "Er nimmt Grinch mit nach Hause. Der Tierarzt ist weit weg, mehr als hundert Kilometer.")
pl("Grinch has two fractures in the pelvis. He cannot get up.", "Grinch hat zwei Brüche im Becken. Er kann nicht aufstehen.")
pl("Worcester sleeps on the floor, next to the dog. And he pays the bill from the vet himself.", "Worcester schläft auf dem Boden, neben dem Hund. Und er bezahlt die Rechnung vom Tierarzt selbst.")
pl("A floor with no hay is not a good bed.", "Ein Boden ohne Heu ist kein gutes Bett.")
pl("Then Grinch gets up again. The whole of Kulin loves the dog. The people in Kulin are kind.", "Dann steht Grinch wieder auf. Ganz Kulin liebt den Hund. Die Leute in Kulin sind nett.")
pl("The family in Italy hears about Grinch and flies to Kulin. The arrival is a big moment.", "Die Familie in Italien hört von Grinch und fliegt nach Kulin. Die Ankunft ist ein großer Moment.")
pl("Grinch knows at once: that is Mum, that is Dad. Everyone is happy.", "Grinch weiß sofort: Das ist Mama, das ist Papa. Alle sind glücklich.")
pl("On the second of December Grinch flies to Italy. Worcester says: at the departure I will be very sad. We are really good mates.", "Am zweiten Dezember fliegt Grinch nach Italien. Worcester sagt: Bei der Abfahrt bin ich sehr traurig. Wir sind richtig gute Freunde.")
pl("Does Grinch have a ticket? No. A ticket is for the train. And Italy is far. We are very exact here.", "Hat Grinch eine Fahrkarte? Nein. Eine Fahrkarte ist für den Zug. Und Italien ist weit. Wir sind hier sehr genau.")
pl("And in America: in San Antonio there is a meal for Thanksgiving, for twenty-five thousand people. Free.", "Und in Amerika: In San Antonio gibt es zu Thanksgiving ein Essen für fünfundzwanzigtausend Menschen. Gratis.")
pl("Since the year 1979. This year it is number forty-seven. The address: the convention centre.", "Seit dem Jahr neunzehnhundertneunundsiebzig. Dieses Jahr ist es Nummer siebenundvierzig. Die Adresse: das Kongresszentrum.")
pl("At nine o'clock the doors are open. In the late morning, at half past ten, the food comes.", "Um neun Uhr sind die Türen offen. Am Vormittag, um halb elf, kommt das Essen.")
pl("The bus is free. The guests need no ticket. When they get on, they simply tell the driver: I am going to the meal.", "Der Bus ist gratis. Die Gäste brauchen keine Fahrkarte. Beim Einsteigen sagen sie dem Fahrer nur: Ich fahre zum Essen.")
pl("The bus company says: for registered customers the ride is free. No ticket, no bill. Only a stop and a full plate.", "Die Busfirma sagt: Für registrierte Kunden ist die Fahrt gratis. Keine Fahrkarte, keine Rechnung. Nur eine Haltestelle und ein voller Teller.")

# ---------------- grammar of the day: the future with werden ----------------
spl("The grammar of the day.", "Die Grammatik des Tages.")
en("Pattern of the day: the future with 'werden'. 'werden' takes second place, and the main verb goes to the very end: ich werde, du wirst, er wird, wir werden, sie werden.")
pl("Grinch will fly to Italy on the second of December.", "Grinch wird am zweiten Dezember nach Italien fliegen.")
pl("Sergeant Worcester will drive the dog to Perth.", "Sergeant Worcester wird den Hund nach Perth fahren.")
pl("On Saturday it will rain a lot in Canberra.", "Am Samstag wird es in Canberra viel regnen.")
pl("The Senate will vote again in February.", "Der Senat wird im Februar wieder abstimmen.")
pl("With the law, from the year 2028 up to twenty per cent of the gas will stay in Australia.", "Mit dem Gesetz werden ab dem Jahr zweitausendachtundzwanzig bis zu zwanzig Prozent vom Gas in Australien bleiben.")
pl("The central bank will decide on the eighth of December.", "Die Zentralbank wird am achten Dezember entscheiden.")
pl("Kushner says: the exchange of prisoners will come soon.", "Kushner sagt: Der Austausch von Gefangenen wird bald kommen.")
pl("And tomorrow we will hear the news again.", "Und morgen werden wir wieder die Nachrichten hören.")

# ---------------- recap ----------------
spl("In short.", "Kurz gesagt.")
pl("Leah Blyth goes over to One Nation. New party, new address.", "Leah Blyth wechselt zu One Nation. Neue Partei, neue Adresse.")
pl("The law for gas is still not finished. Parliament is empty until February.", "Das Gesetz für Gas ist noch nicht fertig. Das Parlament ist bis Februar leer.")
pl("The rent and the bill for electricity are going up.", "Die Miete und die Rechnung für Strom steigen.")
pl("In Kuwait two Italians die. Offers back and forth, but no solution.", "In Kuwait sterben zwei Italiener. Angebote hin und her, aber keine Lösung.")
pl("In Kyiv a missile hits a building with many shops.", "In Kiew trifft eine Rakete ein Haus mit vielen Geschäften.")
pl("Grinch the dog can get up again. He is happy and flies home, to Italy.", "Der Hund Grinch kann wieder aufstehen. Er ist glücklich und fliegt nach Hause, nach Italien.")

# ---------------- words of the day ----------------
spl("The words of the day.", "Die Wörter des Tages.")
pl("the customer", "der Kunde")
pl("The customers get high bills.", "Die Kunden bekommen hohe Rechnungen.")
pl("engaged, taken, occupied", "besetzt")
pl("The line is engaged.", "Die Leitung ist besetzt.")
pl("nice, kind", "nett")
pl("The people in Kulin are kind.", "Die Leute in Kulin sind nett.")
pl("would like", "möchten")
pl("It would like only oats.", "Es möchte nur Hafer.")
pl("the stop", "die Haltestelle")
pl("Today, do not wait long at the stop!", "Heute nicht lange an der Haltestelle warten!")
pl("the arrival", "die Ankunft")
pl("The arrival is a big moment.", "Die Ankunft ist ein großer Moment.")
pl("next to", "neben")
pl("Worcester sleeps on the floor, next to the dog.", "Worcester schläft auf dem Boden, neben dem Hund.")
pl("the departure", "die Abfahrt")
pl("Worcester says: at the departure I will be very sad.", "Worcester sagt: Bei der Abfahrt bin ich sehr traurig.")
pl("the late morning", "der Vormittag")
pl("In the late morning it is perhaps still dry.", "Am Vormittag ist es vielleicht noch trocken.")

# ---------------- close ----------------
pl("That was the news, straight from the horse's mouth. Goodbye, listeners. See you tomorrow.", "Das waren die Nachrichten, direkt vom Pferd. Auf Wiederhören, liebe Hörer. Bis morgen.")
p1pl("Now everything again, in German only.", "Jetzt alles noch einmal, nur auf Deutsch.")

JOB = "jobs/0097-news-2026-11-27.json"
job = {
 "type": "news", "lang": "de", "voice_de": "de_DE-thorsten-medium", "speed_de": 1.0,
 "date": "2026-11-27", "music": "v5",
 "title": "Ex Ōre Equī · Deutsch · Freitag (Fri 27 Nov 2026)",
 "summary": ("First German episode. Canberra: 15–28°, cloudy, showers mostly afternoon/evening, 60%, thunderstorm possible, UV 11. Saturday 16–25°, 95%, 15–45 mm, storms possible. "
             "Sydney 27, Melbourne 25 (rain, storm), Brisbane 29 (showers), Perth 27 (sunny), Adelaide 28, Hobart 26 (evening showers), Darwin 35 (showers, storm). "
             "Australia: SA Liberal senator Leah Blyth (shadow ministry) defects to One Nation: 'I can no longer in good conscience tell Australians that the Liberal Party can save this country'; "
             "Taylor 'disappointing'; Abbott 'nothing whatsoever to do with principle'; Albanese: Taylor 'can't even run his own frontbench', inflation 4.9% 'too high'. "
             "October CPI 4.9%, electricity +25.2%, rents +3.5%; RBA decides 8 Dec 2:30 pm, big banks expect no hike. Gas reserve bill passes second reading 21–10, final vote in February; "
             "Coalition will not oppose (McDonald: 'reliable and affordable gas'); Ayres: 'affordable gas for business and for households'; up to 20% reserved from Jan 2028. "
             "Iran: drones hit an air-defence station in Kuwait, two Italian Rheinmetall Italia technicians killed, a Pakistani and a Kuwaiti captain hurt; Kuwait: 'heinous Iranian aggression'; "
             "Meloni: 'tragic deaths'; Iran denies; IRGC claims two tankers hit mines (unverified); UKMTO: two tankers hit, crews safe; Bessent: no Iranian oil on the water; "
             "Qatar and Pakistan pass proposals; Araghchi 'examining ideas'; Kushner: 'all his options on the table'; Brent ~$94 Thursday. "
             "Ukraine: 113 drones + ballistic missiles, 87 down, hits at 20 locations; Kharkiv 3 killed; Kyiv shopping centre hit, 7 injured; "
             "Zelensky: another massive strike being prepared; Trump: 'A COMPLETE BLOODBATH', wants Putin to pull back; Kushner: Putin 'a grandmaster of politics', not interested in a ceasefire, "
             "POW swap 'very soon, before the holidays', the biggest of the war; Putin's Direct Line 10 Dec. "
             "Good news: Sgt David Worcester of Kulin WA cared for Grinch, the service dog of an Italian tourist killed in a crash; Grinch flies home to Italy on 2 Dec (ABC). "
             "San Antonio: 47th Raul Jimenez Thanksgiving Dinner, 25,000 guests, free VIA buses (KSAT). Grammar of the day: the future with werden. "
             "Every line in English, then German; then all the German again. "
             "Sources: Bureau of Meteorology; Reuters via Devdiscourse; Business Upturn; ABC; AAP/Yahoo; The Nightly; Savings.com.au; Broker Daily; i24NEWS; Times of Israel/AFP; "
             "Reuters via BOE Report and RTÉ; CBS; Dawn; Anadolu; Interfax-Ukraine; Euronews; AP; Spotmedia; Kyiv Post; Kyiv Independent; KSAT."),
 "lines": L,
}

# target words (cards first answered 25–26 Nov): regex per word
TARGETS = {
 "die Rechnung": r"\bRechnung(en)?\b", "günstig": r"\bgünstig\w*", "die Fahrkarte": r"\bFahrkarte\w*",
 "die Abfahrt": r"\bAbfahrt\b", "das Geschäft": r"\bGeschäft\w*", "noch": r"\bnoch\b", "weit": r"\bweit(e[rnms]?)?\b",
 "ruhig": r"\bruhig\w*", "die Miete": r"\bMiete\b", "die Lösung": r"\bLösung\b", "ganz": r"\bganz(e[nmrs]?)?\b",
 "neben": r"\bneben\b", "die Adresse": r"\bAdresse\b", "fertig": r"\bfertig\b", "die Ankunft": r"\bAnkunft\b",
 "die Haltestelle": r"\bHaltestelle\b", "glücklich": r"\bglücklich\w*", "das Angebot": r"\bAngebot\w*",
 "aufstehen": r"\b(aufstehen|steh\w*( \w+){0,3} auf\b)", "umsteigen": r"\b(umsteigen|steig\w*( \w+){0,4} um\b)", "der Rücken": r"\bRücken\b",
 "der Kunde": r"\bKunde\w*", "der Ort": r"\bOrte?\b", "der Nachmittag": r"\bNachmittag\b", "der Vormittag": r"\bVormittag\b",
 "möchten": r"\bmöcht\w*", "das Jahr": r"\bJahr\w*", "nett": r"\bnett\w*", "besetzt": r"\bbesetzt\w*", "leer": r"\bleer\b",
}

if __name__ == "__main__":
    json.dump(job, open(JOB, "w"), ensure_ascii=False, indent=1)
    de = [r[-1] for k, *r in L if k != 'en']
    w = sum(len(t.split()) for t in de)
    bad = [t for t in de if re.search(r'\d', t)]
    print(len(L), 'lines ·', len(de), 'German lines ·', w, 'German words · digits:', bad)
    txt = "\n".join(de)
    low = []
    for k, rx in TARGETS.items():
        n = len(re.findall(rx, txt, re.I))
        print(f"  {k}: {n}")
        if n < 3: low.append(k)
    print("TARGETS UNDER 3:", low)
