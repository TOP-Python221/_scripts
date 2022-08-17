from pprint import pprint

people = [
	{
		'name': "Donovan Buck",
		'email': "tellus.imperdiet@aol.edu",
		'langs': "IT KZ EN"
	},
	{
		'name': "Hanae Robbins",
		'email': "aliquam.adipiscing.lacus@aol.edu",
		'langs': "DE CH SP"
	},
	{
		'name': "Edward Cash",
		'email': "ut.lacus@protonmail.edu",
		'langs': "IT CH FR RU"
	},
	{
		'name': "Kamal Blevins",
		'email': "ante.bibendum@hotmail.net",
		'langs': "FR IT CH EN"
	},
	{
		'name': "Macey Ellis",
		'email': "ornare@yahoo.org",
		'langs': "DE FR EN"
	},
	{
		'name': "Myles Torres",
		'email': "vel.mauris.integer@google.couk",
		'langs': "CH DE IT FR"
	},
	{
		'name': "Macy Nichols",
		'email': "turpis.nulla@outlook.net",
		'langs': "CH FR RU DE"
	},
	{
		'name': "Moana Powers",
		'email': "auctor.velit.eget@protonmail.com",
		'langs': "EN SP KZ IT"
	},
	{
		'name': "Raja Hale",
		'email': "sem.ut@icloud.edu",
		'langs': "DE KZ CH"
	},
	{
		'name': "Jermaine Wells",
		'email': "sit.amet@icloud.edu",
		'langs': "IT FR"
	},
	{
		'name': "Veronica Lawrence",
		'email': "erat.nonummy.ultricies@google.net",
		'langs': "EN IT RU"
	},
	{
		'name': "Jared Yang",
		'email': "neque@protonmail.com",
		'langs': "KZ IT SP"
	},
	{
		'name': "Florence Butler",
		'email': "aliquet.molestie@icloud.ca",
		'langs': "DE EN SP"
	},
	{
		'name': "Debra Mejia",
		'email': "elementum@protonmail.ca",
		'langs': "KZ RU SP"
	},
	{
		'name': "Callie Carson",
		'email': "posuere@aol.com",
		'langs': "EN SP CH"
	},
	{
		'name': "Azalia Douglas",
		'email': "sapien@protonmail.com",
		'langs': "RU KZ SP FR"
	},
	{
		'name': "Colt Nunez",
		'email': "lectus.pede@yahoo.couk",
		'langs': "RU DE EN FR CH"
	},
	{
		'name': "Shelley Sloan",
		'email': "eget.mollis.lectus@aol.ca",
		'langs': "SP KZ EN"
	},
	{
		'name': "Jameson Higgins",
		'email': "aliquam.erat@icloud.ca",
		'langs': "SP EN FR DE IT"
	},
	{
		'name': "Wing Hammond",
		'email': "porttitor@yahoo.ca",
		'langs': "FR DE"
	},
	{
		'name': "Celeste Sutton",
		'email': "aliquam.arcu.aliquam@icloud.net",
		'langs': "EN RU DE SP"
	},
	{
		'name': "Colt Mclean",
		'email': "fringilla.mi@protonmail.edu",
		'langs': "RU EN IT"
	},
	{
		'name': "Mollie Hubbard",
		'email': "sit.amet@aol.com",
		'langs': "RU FR DE"
	},
	{
		'name': "Michelle Hickman",
		'email': "ac.metus.vitae@yahoo.com",
		'langs': "EN RU"
	},
	{
		'name': "Quamar Thomas",
		'email': "montes.nascetur@icloud.net",
		'langs': "FR DE IT KZ"
	},
	{
		'name': "Yoshi Mosley",
		'email': "ac@icloud.couk",
		'langs': "KZ SP DE EN"
	},
	{
		'name': "Carolyn Mann",
		'email': "quisque.imperdiet.erat@outlook.com",
		'langs': "SP IT CH"
	},
	{
		'name': "Morgan Bird",
		'email': "vivamus.molestie.dapibus@protonmail.com",
		'langs': "SP DE KZ FR"
	},
	{
		'name': "Macey York",
		'email': "tincidunt@yahoo.com",
		'langs': "SP KZ FR"
	},
	{
		'name': "Hamish Chen",
		'email': "non.luctus.sit@aol.couk",
		'langs': "SP IT RU DE"
	},
	{
		'name': "Jakeem Donovan",
		'email': "proin.sed.turpis@yahoo.couk",
		'langs': "RU SP CH"
	},
	{
		'name': "Wing Berry",
		'email': "suscipit.nonummy@icloud.org",
		'langs': "RU FR"
	},
	{
		'name': "Erich Burt",
		'email': "fringilla.purus@outlook.com",
		'langs': "SP FR CH RU"
	},
	{
		'name': "Zeus George",
		'email': "sed@hotmail.org",
		'langs': "FR RU"
	},
	{
		'name': "Germaine Warner",
		'email': "aenean.gravida@aol.net",
		'langs': "DE IT CH EN"
	},
	{
		'name': "Amal Benson",
		'email': "cum.sociis.natoque@google.org",
		'langs': "FR RU IT"
	},
	{
		'name': "Jordan Walton",
		'email': "nulla.cras@hotmail.edu",
		'langs': "KZ IT RU EN CH"
	},
	{
		'name': "Edward Kelley",
		'email': "vel.est@protonmail.org",
		'langs': "CH DE RU"
	},
	{
		'name': "Aidan Malone",
		'email': "curabitur.vel@icloud.couk",
		'langs': "FR DE KZ"
	},
	{
		'name': "Idola Steele",
		'email': "nisi.sem.semper@yahoo.couk",
		'langs': "CH EN"
	},
	{
		'name': "Brendan Slater",
		'email': "vivamus@aol.com",
		'langs': "DE IT KZ"
	},
	{
		'name': "Ali Hawkins",
		'email': "varius.et@outlook.edu",
		'langs': "SP EN DE"
	},
	{
		'name': "Brandon Gomez",
		'email': "odio.nam@hotmail.org",
		'langs': "CH IT KZ DE EN"
	},
	{
		'name': "Kermit Newman",
		'email': "enim.commodo@outlook.edu",
		'langs': "FR SP IT EN KZ"
	},
	{
		'name': "Rana Luna",
		'email': "curae.donec@protonmail.org",
		'langs': "DE CH SP KZ RU"
	},
	{
		'name': "Alexander Cain",
		'email': "diam.duis@hotmail.org",
		'langs': "FR RU KZ IT EN"
	},
	{
		'name': "Burton Crosby",
		'email': "euismod@icloud.org",
		'langs': "EN IT KZ"
	},
	{
		'name': "Elizabeth Carver",
		'email': "quis@google.ca",
		'langs': "IT RU DE EN"
	},
	{
		'name': "Lesley Farrell",
		'email': "sem.molestie@protonmail.org",
		'langs': "IT RU FR SP"
	},
	{
		'name': "Colt Byers",
		'email': "bibendum.ullamcorper.duis@outlook.com",
		'langs': "FR EN CH IT"
	},
	{
		'name': "Jescie Donovan",
		'email': "mi@hotmail.couk",
		'langs': "FR IT DE"
	},
	{
		'name': "Malcolm Carver",
		'email': "elementum.at@icloud.edu",
		'langs': "IT EN KZ RU FR"
	},
	{
		'name': "Talon Short",
		'email': "dolor@protonmail.org",
		'langs': "DE EN RU"
	},
	{
		'name': "Aileen Mcclain",
		'email': "sagittis@google.net",
		'langs': "RU CH EN FR KZ"
	},
	{
		'name': "Kuame Knowles",
		'email': "dictum.magna@protonmail.couk",
		'langs': "EN DE KZ FR"
	},
	{
		'name': "Whilemina Wilkinson",
		'email': "mollis.nec@aol.edu",
		'langs': "CH SP EN"
	},
	{
		'name': "Rigel Benton",
		'email': "ante.vivamus@icloud.com",
		'langs': "IT FR CH"
	},
	{
		'name': "Cecilia Drake",
		'email': "auctor.velit@protonmail.edu",
		'langs': "FR CH KZ EN"
	},
	{
		'name': "Meredith Robbins",
		'email': "ac.arcu@hotmail.org",
		'langs': "EN CH KZ IT"
	},
	{
		'name': "Phoebe Burks",
		'email': "ipsum@hotmail.net",
		'langs': "CH KZ"
	},
	{
		'name': "Leo Elliott",
		'email': "et@yahoo.com",
		'langs': "EN SP FR CH"
	},
	{
		'name': "Ursula Foley",
		'email': "fringilla.cursus@yahoo.couk",
		'langs': "CH EN DE SP"
	},
	{
		'name': "Linus Atkinson",
		'email': "dolor.sit@protonmail.ca",
		'langs': "DE KZ RU IT"
	},
	{
		'name': "Denise Bullock",
		'email': "nec@icloud.couk",
		'langs': "EN FR"
	},
	{
		'name': "Dana Calhoun",
		'email': "eu.dui.cum@google.edu",
		'langs': "CH EN SP"
	},
	{
		'name': "Ira Dominguez",
		'email': "enim.sed@hotmail.edu",
		'langs': "EN KZ SP FR"
	},
	{
		'name': "Alana Morgan",
		'email': "purus.maecenas@yahoo.couk",
		'langs': "RU IT EN"
	},
	{
		'name': "Kaitlin Harris",
		'email': "purus@google.net",
		'langs': "KZ FR RU DE"
	},
	{
		'name': "Chloe Hayden",
		'email': "luctus.lobortis@google.org",
		'langs': "CH FR"
	},
	{
		'name': "Martina Stanley",
		'email': "risus.varius@google.net",
		'langs': "KZ CH EN"
	},
	{
		'name': "Kasper Knowles",
		'email': "nisl@google.edu",
		'langs': "DE SP IT KZ"
	},
	{
		'name': "Derek Conner",
		'email': "faucibus.leo.in@google.org",
		'langs': "SP KZ CH RU IT"
	},
	{
		'name': "Angelica Park",
		'email': "morbi.vehicula.pellentesque@protonmail.ca",
		'langs': "IT FR CH DE"
	},
	{
		'name': "Amity Stephenson",
		'email': "tempor.diam@outlook.org",
		'langs': "CH IT DE FR"
	},
	{
		'name': "Mariam Lindsay",
		'email': "mollis.dui.in@outlook.net",
		'langs': "CH DE RU"
	},
	{
		'name': "Jelani Logan",
		'email': "aenean.gravida@yahoo.net",
		'langs': "CH IT KZ"
	},
	{
		'name': "Palmer Stewart",
		'email': "gravida.mauris.ut@aol.couk",
		'langs': "SP IT"
	},
	{
		'name': "Thomas Olson",
		'email': "varius@outlook.couk",
		'langs': "DE RU FR IT"
	},
	{
		'name': "Xaviera Sherman",
		'email': "ipsum.dolor.sit@yahoo.net",
		'langs': "IT EN CH"
	},
	{
		'name': "Elmo Newton",
		'email': "imperdiet.erat@hotmail.org",
		'langs': "RU IT SP EN"
	},
	{
		'name': "Ferdinand Hammond",
		'email': "dui@aol.edu",
		'langs': "SP EN CH DE"
	},
	{
		'name': "Chancellor Stephens",
		'email': "lectus.pede@outlook.org",
		'langs': "RU CH IT FR SP"
	},
	{
		'name': "Vance Osborn",
		'email': "ut.tincidunt@google.edu",
		'langs': "FR SP RU EN"
	},
	{
		'name': "Graiden Glass",
		'email': "suspendisse.tristique@outlook.couk",
		'langs': "DE EN SP CH"
	},
	{
		'name': "Hilel Cantrell",
		'email': "tellus@icloud.net",
		'langs': "FR DE CH"
	},
	{
		'name': "Griffin Alvarez",
		'email': "erat@google.org",
		'langs': "SP DE CH"
	},
	{
		'name': "Lars Bowman",
		'email': "pretium.neque@icloud.org",
		'langs': "EN RU"
	},
	{
		'name': "Hanae Hardy",
		'email': "accumsan.sed@yahoo.net",
		'langs': "RU SP DE"
	},
	{
		'name': "Velma Hicks",
		'email': "arcu.curabitur.ut@icloud.ca",
		'langs': "CH KZ DE"
	},
	{
		'name': "Sylvester Fowler",
		'email': "auctor@yahoo.couk",
		'langs': "CH RU DE"
	},
	{
		'name': "Conan Frye",
		'email': "libero.est.congue@outlook.edu",
		'langs': "DE IT CH FR"
	},
	{
		'name': "Russell Levine",
		'email': "sit.amet@outlook.net",
		'langs': "IT DE RU FR"
	},
	{
		'name': "Kibo Rhodes",
		'email': "amet.risus@protonmail.couk",
		'langs': "EN FR SP RU"
	},
	{
		'name': "Bree Henry",
		'email': "non.leo@aol.com",
		'langs': "EN FR RU"
	},
	{
		'name': "Karen Hanson",
		'email': "scelerisque.dui@outlook.com",
		'langs': "KZ FR CH"
	},
	{
		'name': "Farrah Whitley",
		'email': "vulputate@hotmail.net",
		'langs': "IT RU FR KZ"
	},
	{
		'name': "Nicole Foley",
		'email': "aenean.gravida@aol.edu",
		'langs': "CH FR KZ DE"
	},
	{
		'name': "Uma Norton",
		'email': "luctus@hotmail.org",
		'langs': "CH IT DE FR"
	},
	{
		'name': "Scarlet George",
		'email': "per.inceptos.hymenaeos@protonmail.ca",
		'langs': "CH RU IT KZ"
	},
	{
		'name': "Reese Shields",
		'email': "suscipit@protonmail.couk",
		'langs': "FR KZ EN DE SP"
	},
	{
		'name': "Stewart Brock",
		'email': "elementum.dui@hotmail.edu",
		'langs': "CH DE SP"
	},
	{
		'name': "Olivia Barker",
		'email': "viverra.donec@icloud.net",
		'langs': "CH SP"
	},
	{
		'name': "Gannon Parsons",
		'email': "augue@outlook.ca",
		'langs': "IT RU"
	},
	{
		'name': "Iona Parsons",
		'email': "ac.urna.ut@hotmail.org",
		'langs': "KZ CH RU DE EN"
	},
	{
		'name': "Scott Atkins",
		'email': "morbi@protonmail.org",
		'langs': "EN RU SP KZ"
	},
	{
		'name': "Xaviera Maxwell",
		'email': "ullamcorper@yahoo.edu",
		'langs': "RU DE EN"
	},
	{
		'name': "Hayden Dillard",
		'email': "arcu@yahoo.ca",
		'langs': "FR KZ SP"
	},
	{
		'name': "Chelsea George",
		'email': "ut.quam.vel@outlook.ca",
		'langs': "EN SP RU FR"
	},
	{
		'name': "Lester Edwards",
		'email': "egestas@google.couk",
		'langs': "IT EN DE"
	},
	{
		'name': "Xenos Valencia",
		'email': "bibendum.ullamcorper@google.com",
		'langs': "SP CH KZ"
	},
	{
		'name': "Isabelle Donovan",
		'email': "nibh.donec.est@google.couk",
		'langs': "DE FR"
	},
	{
		'name': "Zelenia Hernandez",
		'email': "nisi.aenean.eget@protonmail.com",
		'langs': "SP IT KZ RU"
	},
	{
		'name': "Germaine Booker",
		'email': "nulla.interdum@google.ca",
		'langs': "IT KZ SP RU EN"
	},
	{
		'name': "Damian Aguirre",
		'email': "quisque@yahoo.edu",
		'langs': "IT KZ EN CH"
	},
	{
		'name': "Shaeleigh Boone",
		'email': "ut.sagittis@yahoo.couk",
		'langs': "KZ SP"
	},
	{
		'name': "Nevada Warren",
		'email': "tellus.sem@icloud.com",
		'langs': "SP CH"
	},
	{
		'name': "Preston Delgado",
		'email': "non.justo@yahoo.couk",
		'langs': "IT SP CH"
	},
	{
		'name': "Venus Gallagher",
		'email': "viverra.maecenas@protonmail.ca",
		'langs': "EN KZ"
	},
	{
		'name': "Keefe Underwood",
		'email': "amet.luctus@hotmail.ca",
		'langs': "IT DE FR"
	},
	{
		'name': "Francesca Noel",
		'email': "ligula.eu@hotmail.net",
		'langs': "EN RU IT DE SP"
	},
	{
		'name': "Hector Clemons",
		'email': "donec@hotmail.org",
		'langs': "DE KZ SP IT"
	},
	{
		'name': "Dora Foreman",
		'email': "vitae.nibh.donec@google.net",
		'langs': "RU DE IT KZ CH"
	},
	{
		'name': "Travis Webb",
		'email': "in@google.ca",
		'langs': "RU FR DE SP"
	},
	{
		'name': "Clementine Nicholson",
		'email': "lorem.vehicula.et@outlook.com",
		'langs': "EN IT KZ"
	},
	{
		'name': "Sonia Gay",
		'email': "accumsan@protonmail.com",
		'langs': "FR CH EN IT"
	},
	{
		'name': "Kellie Harvey",
		'email': "arcu.vestibulum.ante@icloud.com",
		'langs': "IT RU KZ"
	},
	{
		'name': "Amal Savage",
		'email': "arcu.ac.orci@google.net",
		'langs': "SP EN"
	},
	{
		'name': "Shoshana Curry",
		'email': "ac.sem@icloud.couk",
		'langs': "CH KZ IT DE FR"
	},
	{
		'name': "Phyllis Schwartz",
		'email': "phasellus.ornare.fusce@aol.edu",
		'langs': "SP IT"
	},
	{
		'name': "Faith Meyer",
		'email': "justo.faucibus.lectus@hotmail.couk",
		'langs': "CH FR KZ EN"
	},
	{
		'name': "Hasad Petersen",
		'email': "augue.malesuada.malesuada@yahoo.couk",
		'langs': "IT DE FR RU"
	},
	{
		'name': "Winifred Hess",
		'email': "ut@hotmail.com",
		'langs': "DE FR"
	},
	{
		'name': "Rahim French",
		'email': "amet.ornare@yahoo.edu",
		'langs': "IT FR CH EN RU"
	},
	{
		'name': "Amber Hardy",
		'email': "quis.urna@google.couk",
		'langs': "SP KZ"
	},
	{
		'name': "Mallory Franklin",
		'email': "eros.non@icloud.couk",
		'langs': "IT CH"
	},
	{
		'name': "Micah Rivers",
		'email': "integer@hotmail.edu",
		'langs': "EN FR IT"
	},
	{
		'name': "Wanda Lane",
		'email': "eu.tempor.erat@yahoo.org",
		'langs': "EN CH IT"
	},
	{
		'name': "Sebastian Little",
		'email': "malesuada@yahoo.ca",
		'langs': "IT CH KZ FR"
	},
	{
		'name': "Sylvester Santana",
		'email': "condimentum.donec@google.org",
		'langs': "KZ IT CH EN"
	},
	{
		'name': "Zeph Harrington",
		'email': "nullam.feugiat@protonmail.org",
		'langs': "FR IT KZ RU"
	},
	{
		'name': "Ronan Brock",
		'email': "non@aol.edu",
		'langs': "SP EN IT CH"
	},
	{
		'name': "Laurel West",
		'email': "consectetuer.adipiscing@protonmail.org",
		'langs': "IT EN DE SP"
	},
	{
		'name': "Kasper Lang",
		'email': "sagittis@outlook.ca",
		'langs': "RU EN FR IT CH"
	},
	{
		'name': "Savannah Nichols",
		'email': "pellentesque.ultricies.dignissim@icloud.org",
		'langs': "RU KZ DE"
	},
	{
		'name': "Nyssa Hart",
		'email': "arcu.vel@outlook.edu",
		'langs': "FR IT EN RU"
	},
	{
		'name': "Kane Wolf",
		'email': "elit.a@icloud.org",
		'langs': "DE RU"
	},
	{
		'name': "Aimee Kirby",
		'email': "imperdiet.ullamcorper@aol.com",
		'langs': "IT CH EN KZ FR"
	},
	{
		'name': "Jamal Melendez",
		'email': "nullam@icloud.edu",
		'langs': "SP CH EN DE"
	},
	{
		'name': "Hyacinth Bradford",
		'email': "malesuada@google.net",
		'langs': "EN SP KZ"
	},
	{
		'name': "Wang Larsen",
		'email': "egestas@outlook.net",
		'langs': "SP IT KZ CH"
	}
]

ru_ch_people = [person for person in people 
                if {'RU', 'CH'}.issubset(set(person['langs'].split()))]

pprint(ru_ch_people)
