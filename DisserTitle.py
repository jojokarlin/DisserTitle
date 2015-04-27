#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

ing = [
    "Beyond",
    "Against",
    "Disturbing",
    "Problematizing",
    "Theorizing",
    "Deconstructing",
    "Historicizing",
    "Defining",
    "Reappropriating",
    "Reifying",
    "Moralizing",
    "Appropriating",
    "Elevating",
    "Undermining",
    "Authorizing",
    "Organizing",
    "Galvanizing",
    "Concerning",
    "Discerning",
    "Asserting",
    "Claiming",
    "Interpreting",
    "Antagonizing",
    "Misappropriating",
    "Idealizing",
    "Identifying",
]

ism = [
    "Post-colonialism",
    "Modernism",
    "Absolutism",
    "Abstractionism",
    "Accidentalism",
    "Acosmism",
    "Aestheticism",
    "Agnosticism",
    "Altruism",
    "Anarchism",
    "Anarcho-capitalism",
    "Anarcho-syndicalism",
    "Animism",
    "Anthropocentrism",
    "Anthropomorphism",
    "Antinomianism",
    "Apriorism",
    "Aristotelianism",
    "Asceticism",
    "Ascriptivism",
    "Associationalism",
    "Atheism",
    "Atomism",
    "Authoritarianism",
    "Automatism",
    "Behaviorism",
    "Buddhism",
    "Capitalism",
    "Cartesianism",
    "Christianity",
    "Classicism",
    "Cognitivism",
    "Coherentism",
    "Collectivism",
    "Communalism",
    "Communism",
    "Communitarianism",
    "Compatibilism",
    "Conceptualism",
    "Concretism",
    "Confucianism",
    "Consequentialism",
    "Conservatism",
    "Constructivism",
    "Contextualism",
    "Conventionalism",
    "Cosmism",
    "Creationism",
    "Cynicism",
    "Darwinism",
    "Deconstructionism",
    "Deism",
    "Deontologism",
    "Descriptivism",
    "Determinism",
    "Dialectical materialism",
    "Dogmatism",
    "Dualism",
    "Dynamism",
    "Eclecticism",
    "Egalitarianism",
    "Egoism",
    "Emanationism",
    "Emotionalism",
    "Emotivism",
    "Empiricism",
    "Environmentalism",
    "Epicureanism",
    "Epiphenomenalism",
    "Equalitarianism",
    "Essentialism",
    "Eternalism",
    "Ethnocentrism",
    "Eudaimonism",
    "Existentialism",
    "Experientialism",
    "Experimentalism",
    "Expressionism",
    "Externalism",
    "Fallibilism",
    "Falsificationism",
    "Fascism",
    "Fatalism",
    "Feminism",
    "Fideism",
    "Finalism",
    "Formalism",
    "Foundationalism",
    "Freudianism",
    "Functionalism",
    "Gnosticism",
    "Hedonism",
    "Hegelianism",
    "Henotheism",
    "Historical determinism",
    "Historicism",
    "Holism",
    "Humanism",
    "Hylozoism",
    "Idealism",
    "Illusionism",
    "Immaterialism",
    "Immoralism",
    "Immortalism",
    "Imperativism",
    "Incompatibilism",
    "Indeterminism",
    "Individualism",
    "Inductivism",
    "Instrumentalism",
    "Intellectualism",
    "Intentionalism",
    "Interactionism",
    "Internalism",
    "Interpretivism",
    "Intrinsicism",
    "Intuitionism",
    "Irrationalism",
    "Islam",
    "Ism",
    "Kantianism",
    "Legalism",
    "Liberalism",
    "Libertarianism",
    "Logical positivism",
    "Logicism",
    "Manicheism",
    "Marxism",
    "Materialism",
    "Mechanism",
    "Meliorism",
    "Mentalism",
    "Modernism",
    "Monism",
    "Monotheism",
    "Mysticism",
    "Nativism",
    "Naturalism",
    "Necessitarianism",
    "Neo-Aristotelianism",
    "Neo-Confucianism",
    "Neo-Marxism",
    "Neo-Platonism",
    "Nihilism",
    "Nominalism",
    "Objectivism",
    "Occasionalism",
    "Operationalism",
    "Optimism",
    "Organicism",
    "Pacifism",
    "Panpsychism",
    "Pantheism",
    "Particularism",
    "Perfectionism",
    "Personalism",
    "Perspectivism",
    "Pessimism",
    "Phenomenalism",
    "Physicalism",
    "Platonism",
    "Pluralism",
    "Polylogism",
    "Polytheism",
    "Positivism",
    "Postmodernism",
    "Pragmatism",
    "Prescriptivism",
    "Probabilism",
    "Progressivism",
    "Psychologism",
    "Pyrrhonism",
    "Pythagoreanism",
    "Randianism",
    "Rationalism",
    "Realism",
    "Reductionism",
    "Relationalism",
    "Relativism",
    "Representationalism",
    "Romanticism",
    "Scholasticism",
    "Scientism",
    "Secularism",
    "Sensationalism",
    "Sensualism",
    "Situationalism",
    "Skepticism",
    "Social Darwinism",
    "Socialism",
    "Socraticism",
    "Solipsism",
    "Spiritualism",
    "Statism",
    "Stoicism",
    "Structuralism",
    "Subjectivism",
    "Substantialism",
    "Symbolism",
    "Syncretism",
    "Taoism",
    "Teleologism",
    "Theism",
    "Thomism",
    "Totalitarianism",
    "Transcendentalism",
    "Universalism",
    "Utilitarianism",
    "Utopianism",
    "Verificationism",
    "Vitalism",
    "Voluntarism",
    "Voluntaryism",
    "Zoroastrianism",
    ]

verb = [
    "Defines",
    "Assigns",
    "Categorizes",
    ]

"""
trans_verb = [
    "inspires",
    "jabs",
    "pokes",
    "smudges",
    "nudges",
    "prods",
    "gazes at",
    "admires",	
    "gazes at",	
    "peeks at",	
    "peers at",	
    "bargains with",	
    "deals with",	
    "plots with",	
    "conspires to",	
    "oozes",
     "adores",	
    "amuses",	
    "cherishes",	
    "treasures",	
    "despises",	
    "loathes",
     "casts",	
    "catapults",	
    "hurls",	
    "lobs",
     "modifies",	
    "morphs into",	
    "entertains",	
      "liquefies",	
    "brews",	
    "extracts",	
    "alters",
      "assaults",	
    "disarms",	
 """

prep = [
    
    "on",
    "in",
    "of",
    "opposite",
    "with",
    "after",
    "beside",
    "along with",
    "instead of",
    "for",
    "behind",
    ]

adj = [
    "Victorian",
    "New Historical",
    "Mystical",
    "Political",
    "Practical",
    "Technological",
    "Industrial",
    "Mercantile",
    "Hegemonic",
    "Phenomenologic",
    "Sausserian",
    "Foucauldian",
    "Post-apocalyptic",
    "Utopian",
        ]

obj = [
    "Miasma",
    "Misanthropy",
    "Bodies",
    "Symbiosis",
    "Systems",
    "Time-Space",
    "Massacre",
    "Biology",
    "Physics",
    "Topography",
    "England",
    "Fiction",
    "Comedy",
    "Cultural Studies",
    "Britain",
    "Pangea",
    "America",
    "Trade Routes",
    "Customs",
    "Tea Towels",
    "Vernacular",
    "Early Modernism",
    "Dogma",
    "Drama",
    "Ritual",
    "Empire",
    "Monarchy",
    "Practice",
    "Religion",
    "Environments",
    "Climate", 
    "Myopia",
    "Politics",
    "Enclosure",
    "Practice"
    ]

def diss_gen():
    return("%s %s: %s %s %s %s %s." %(random.choice(ing),random.choice(ism),random.choice(ing),random.choice(ism), random.choice(prep),random.choice(adj), random.choice(obj)))

print(diss_gen())


tfile = open("diss_tweets.txt", "w")
for numtweets in range(0,1000):
    tfile.write(diss_gen())
    tfile.write("\n")

tfile.close()
