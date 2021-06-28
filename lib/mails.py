#!/usr/bin/env python3

"""
This file is the mapping between email adresses and the new recipe 
directory/mailbox where mail will be dropped to.

The approch is simple and trivial pattern matching recognition and does not use any machine learning
algorithm.

Since addresses are very exhausted, my change, etc.
It's is clear the this is not an efficient way to operate but it was a begining to learn Python
and handle pattern matching in Python.
"""

my_addr = {}
ext_addr ={}


my_addr = {
             ('perl@mongueurs.net','s')         : 'ml/ppm',
             ('paris@mongueurs.net','s')        : 'ml/ppm',
             ('@pm.org','s')                    : 'ml/ppm',
             ('@parinux.org','s')               : 'ml/linux',
             ('@lists.parinux.org','s')         : 'ml/linux',
             ('tunixie@free.fr','s')            : 'ml/linux',
             ('alain tesio','s')                : 'ml/linux',
             ('jerome kieffer','s')             : 'ml/linux',
             ('oliviero patrick','s')           : 'ml/linux',
             ('laurent martelli','s')           : 'ml/linux',
             ('juliette.risi@free.fr','s')      : 'ml/linux',
             ('sylvain@lhullier.org','s')       : 'ml/linux',
             ('@cartron.org','s')               : 'ml/cartron',
             ('selistes-internautes-echanges@yahoogroupes.fr','s' )     : 'ml/Sel92',
             ('selrueil92-echanges@yahoogroupes.fr','s')                : 'ml/Sel92',
             ('idf-intersel@yahoogroupes.fr','s')                       : 'ml/Sel92',
             ('rv.seliste-internaute@orange.fr','s')                    : 'ml/Sel92',
             ('selrueil92-echanges-proprietaire@yahoogroupes.fr','s')   : 'ml/Sel93',
             ('pays-gallo.net>','s')            : 'ml/pays_gallo',
             ('@attac.org','s')                 : 'ml/attac',
             ('Liste francophone pour les questions.+ sur Perl','m') : 'ml/ppm',
             ('ryad@karar.fr','s')              : 'karar',
             ('drnmode@aol.com','s')            : 'Drnmode',
             ('bruneteau.sabine@(free|orange).fr','m')  : 'SABINE',
             ('infosclient@ceisame.fr','s') :  'Ceisame/ceisame',
             ('pole-emploi\.(net|fr)>','m')     : 'travail/pole_emploi',
             ('@cp.tsce.net','s')               : 'travail/pole_emploi',
             ('@pole-emploi.info','s')          : 'travail/pole_emploi',
             ('@email.pagepersonnelle.fr','s')  : 'travail/pagepersonnel',
             ('@email.pagepersonnel','s')       : 'travail/pagepersonnel',
             ('@pagepersonnel.fr>','s')         : 'travail/pagepersonnel',
             ('infos@sevigne.com','s')          : 'hiscox',
             ('velizymodsept@free.fr','s')      : 'ml/velizymodsept',
             ('velizymodsept-request@ml.free.fr','s') : 'ml/velizymodsept',
             ('deville.julie@orange.fr','s')   : 'julie_deville',
             ('deville.julie@wanadoo.fr','s')  : 'julie_deville',
             ('@lesjeudis.com','s')            : 'travail/lesjeudis',
             ('lesjeudis.com>','s')            : 'travail/lesjeudis',
             ('lesjeudis.cccampaigns.net','s') : 'travail/lesjeudis',
             ('veroniquep@wanadoo.fr','s')     : 'reseaux_sociaux/LaMaiZon',
             ('etreville@aaescp-eap.net','s')  : 'reseaux_sociaux/LaMaiZon',
             ('la-couarde-atlantik@wanadoo.fr','s') : 'reseaux_sociaux/LaMaiZon',
             ('jobs@itjobboard.nl','s')        : 'travail/ItJobBoard',
             ('theitjobboard.com','s')         : 'travail/ItJobBoard',
             ('@theunixjobboard.com','s')      : 'travail/ItJobBoard',
             ('@idppmail.com','s')             : 'travail/IdppMail',
             ('sybase.com','s')                : 'pub/Sybase',
             ('@amazon.fr','s')                : 'pub/Amazon',
             ('francois.gillier@atosorigin.com','s') : 'francois.gillier',
             ('[\.@]jobintree.com','m')        : 'travail/jobintree',
             ('@freelance.com','s')            : 'travail/freelance_com',
             ('@valor.fr','s')                 : 'travail/freelance.com',
             ('@collectifpsychiatrie.fr','s')  : 'politique/NuitSecuritaire',
             ('sandrine.durandiere@free.fr','s')  : 'sandrine_durandiere',
              ('@(info\.)?(dreamteam-portage|@groupe-freeteam)\.com>','m') : 'travail/dreamteam',
              ('caf.fr>','s' )         : 'CAF',
              ('@inops.fr>','s' )                        : 'travail/INOPS',
              ('@bdl-saintamand.fr>','s')                : 'BDL_COMPTABILITE'
            }

ext_addr ={
             ('jeanyves.daniel@free.fr','s')   : 'outbox/jeanyves.daniel',
             ('pim.mouss@free.fr','s')         : 'outbox/pim.mouss',
             ('pim.mousse@free.fr','s')        : 'outbox/pim.mousse',
             ('^pim ','m')                     : 'outbox/Pim',
             ('^jean-yves daniel','m')         : 'outbox/JeanYvesDaniel',
             ('^root ','m')                    : 'outbox/Root',
             ('^pimouse ','m')                 : 'outbox/Pimouse',
             ('maberrilia@free.fr','s')        : 'Marie_claire',
             ('hubjoss@hotmail.fr','s')        : 'Marie_claire',
             ('paam.daniel@free.fr','s')       : 'Patrick',
             ('gigidecost@hotmail.com','s')    : 'Gisele',
             ('laurence-p.jost@laposte.net','s'): 'laurence_jost',
             ('laurence.jost@sisley.tm.fr','s') : 'laurence_jost',
             ('lorina95@yahoo.fr','s')          : 'laurence_jost',
             ('cdouette@laposte.net','s')      : 'Claudie',
             ('decogis@hotmail.com','s')       : 'Gisele',
             ('pascaloudaniel@gmail.com','s')  : 'Pascal',
             ('pascal.daniel@euroson.fr','s')  : 'Pascal',
             ('gliemjo@gmail.com','s')         : 'Hachim',
             ('@cartron.org','s')               : 'ml/cartron',
             ('gisougliem@hotmail.com','s')    : 'Gizella',
             ('theo.daniel3@free.fr','s')      : 'neveu/theo',
             ('deville.julie@orange.fr','s')   : 'julie_deville',
             ('deville.julie@wanadoo.fr>','s') : 'julie_deville',
             ('mh.daniel@free.fr','s')         : 'cousin/hub_daniel',
             ('nadia.aballache@hotmail.fr','s') :'Nadia', 
             ('manli.prisciandaro','s')        : 'Manli',
             ('alain-hubert@wanadoo.fr','s')   : 'alain_hubert',
             ('lautre75@gmail.com','s')        : 'laurence_trebucq',
             ('stephan.larsen@lebedev.com','s'): 'stephane_larsen',
             ('jean.marchalant@free.fr','s')   : 'jc.marchalant',
             ('maryz.b-647484@sfr.fr','s')     : 'Maryse',
             ('francois.gillier@atosorigin.com','s') : 'francois.gillier',
             ('@dgfip.finances.gouv.fr','s')   : 'impots/impots',
             ('@onvasortir.com','s')           : 'reseaux_sociaux/ovs',
             ('asso-des-solos.fr','s')         : 'reseaux_sociaux/Solos',
             ('@badoo.com','s')                : 'rencontres/badoo',
             ('@meetic.com','s')               : 'rencontres/meetic',
             ('@netclub.com','s')              : 'rencontres/netclub',
             ('@lovoo.com','s')                : 'rencontres/Lovoo',
             ('@adopteunmec.com','s')          : 'rencontres/adoptesUnmec',
             ('nadinenachez9@gmail.com','s')   : 'nadine',
             ('malamzadeh@yahoo.fr','s')       : 'masoud_alamzadeh',
             ('malamzadeh@voila.fr','s')       : 'masoud_alamzadeh', 
             ('bruneteau.sabine@(free|orange).fr','m')  : 'SABINE',
             ('saabnam@free.fr','s')           : 'SABINE',
             ('y_beh@yahoo.fr','s')            : 'YvesAlain',
             ('perl@mongueurs.net','s')        : 'ml/ppm',
             ('paris@mongueurs.net','s')       : 'ml/ppm',
             ('@pm.org','s')                   : 'ml/ppm',
             ('@parinux.org','s')              : 'ml/linux',
             ('@lists.parinux.org','s')        : 'ml/linux',
             ('tunixie@free.fr','s')           : 'ml/linux',
             ('alain tesio','s')               : 'ml/linux',
             ('jerome kieffer','s')            : 'ml/linux',
             ('oliviero patrick','s')          : 'ml/linux',
             ('laurent martelli','s')          : 'ml/linux',
             ('juliette.risi@free.fr','s')     : 'ml/linux',
             ('sylvain@lhullier.org','s')      : 'ml/linux',
             ('@attac.org','s')                : 'ml/attac',
             ('lists.gossamer-threads.com','s'): 'ml/gossamer',
             ('@mercuriurval.com','s')         : 'ml/mercuriUrval',
             ('@openclassrooms.com','s')       : 'ml/OpenClassrooms',
             ('selistes-internautes-echanges@yahoogroupes.fr','s')      : 'ml/Sel92',
             ('selrueil92-echanges@yahoogroupes.fr','s')                : 'ml/Sel92',
             ('idf-intersel@yahoogroupes.fr','s')                       : 'ml/Sel92',
             ('rv.seliste-internaute@orange.fr','s')                    : 'ml/Sel92',
             ('selrueil92-echanges-proprietaire@yahoogroupes.fr','s')   : 'ml/Sel92',
             ('pays-gallo.net','s')            : 'ml/pays_gallo',
             ('@directassurance(\.bp-email)?\.fr>','m')       : 'assurance/directAssurance',
             ('Liste francophone pour les questions.+ sur Perl','m') : 'ml/ppm',
             ('engie@particuliers.engie.com','s') : 'Electricite',
             ('@email-particuliers.engie.fr>','s') : 'Electricite',
             ('service-clients@particuliers1.engie.com','s') : 'Electricite',
             ('@noreade.fr','s')               : 'Eau',
             ('developpez.com','s')            : 'dev/DeveloppezCom',
             ('instructables.com>','s')        : 'dev/instructables',
             ('@macif.fr','s')                 : 'Macif',
             ('@univ-rennes1.fr','s')          : 'test/echo',
             ('echo@cnam.fr','s')              : 'test/echo',
             ('@dl.free.fr','s')               : 'test/Free',
             ('christian.leon5@sfr.fr','s')    : 'contact/christian_leon',
             ('marie fernandez','s')           : 'contact/marieFernandez',
             ('@cmsmadesimple.fr','s')         : 'contact/CmsMadeSimple',
             ('@sysmic.fr','s')                : 'contact/Sysmic',
             ('@aptus.fr','s')                 : 'contact/Aptus',
             ('socgen.com','s')                : 'contact/societeGenerale',
             ('notaires.fr','s')               : 'contact/Notaire',
             ('tryphonlabidouille','s')        : 'contact/tryphon',
             ('@sunapsis','s')                 : 'travail/Sunapsis',
             ('@free-expert.com','s')          : 'travail/freeExpert',
             ('[\.@]jobintree.com','m')        : 'travail/jobintree',
             ('@degetel.com','s')              : 'travail/degetel',
             ('apec.fr>','s')                  : 'travail/Apec',
             ('@apec.fr','s')                  : 'travail/Apec',
             ('@emagine','s')                  : 'travail/emagine',
             ('@dice.com','s')                 : 'travail/dice',
             ('@freelance.com','s')            : 'travail/freelance_com',
             ('@valor.fr','s')                 : 'travail/freelance.com',
             ('thomas_gaumondie@fr.ibm.com','s'): 'travail/freelance.com',
             ('@maths-fi.com','s')             : 'travail/maths_fi',
             ('@freelance-info.fr','s')        : 'travail/freelance_info',
             ('@lesjeudis.com','s')            : 'travail/lesjeudis',
             ('lesjeudis.com>','s')            : 'travail/lesjeudis',
             ('lesjeudis.cccampaigns.net','s') : 'travail/lesjeudis',
             ('@erecrut.com','s')              : 'travail/Erecrut',
             ('@indeed.com','s')               : 'travail/indeed',
             ('ictjob.be','s')                 : 'travail/Ictjob',
             ('pole-emploi\.(net|fr)>','m')    : 'travail/pole_emploi',
             ('@cp.tsce.net','s')               : 'travail/pole_emploi',
             ('@pole-emploi.info','s')          : 'travail/pole_emploi',
             ('nicolas.elbaz@orange.fr','s')   : 'travail/formation/NicolasElbaz',
             ('@anpe.fr','s')                  : 'travail/anpe',
             ('jobs@itjobboard.nl','s')        : 'travail/ItJobBoard',
             ('theitjobboard.com','s')         : 'travail/ItJobBoard',
             ('@theunixjobboard.com','s')      : 'travail/ItJobBoard',
             ('computerfutures.fr>','s')       : 'travail/ComputerFutures',
             ('@computerfutures.com','s')      : 'travail/ComputerFutures',
             ('computerfutures.be','s')        : 'travail/Belgique/ComputerFutures',
             ('cadremploi.fr','s')             : 'travail/CadreEmploi',
             ('@montreal.co.uk','s')           : 'travail/MontrealAssociates',
             ('@montrealassociates.com','s')   : 'travail/MontrealAssociates',
             ('monster.com','s')               : 'travail/Monster',
             ('linkedin.com','s')              : 'travail/Linkedin',
             ('@addviseo.com','s')             : 'travail/AddViseo',
             ('@codeur.com','s')               : 'travail/CodeurCom',
             ('@progressive-fr.com','s')       : 'travail/Progressive',
             ('@progressive.co.uk','s')        : 'travail/Progressive',
             ('@nwruk.com','s')                : 'travail/nwruk',
             ('@astek.fr','s')                 : 'travail/Astek',
             ('@quaternove.fr','s')            : 'travail/Quaternove',
             ('@progressiverecruitment.com','s'):'travail/Progressive',
             ('@cnet.com','s')                 : 'travail/Cnet',
             ('@chrometechnologies.com','s')   : 'travail/ChromeTechnologies',
             ('@ventura-associate.com','s')    : 'travail/VenturaAssociate',
             ('@consultime.com','s')           : 'travail/consultime',
             ('@arealti.com','s')              : 'travail/arealti',
             ('@michaelpage.fr','s')           : 'travail/michael_page',
             ('e-tangerine','s')               : 'travail/Etangerine',
             ('@smarteo.com','s')              : 'travail/Smarteo',
             ('@offres-emplois.com','s')       : 'travail/tout_surveiller',
             ('@thalesgroup.com','s')          : 'travail/thales',
             ('@informatis','s')               : 'travail/informatis',
             ('@webengineering.fr','s')        : 'travail/WebIngeneering',
             ('@huxley\.(fr|com)','m')         : 'travail/huxley',
             ('@emploi-store.fr','s')          : 'travail/EmploiStore',
             ('@freelancerepublik.com','s')    : 'travail/freelance_republik',
             ('@easypartner.fr','s')           : 'travail/easypartner',
             ('.arealti','s')                  : 'travail/arealti',
             ('@rhperformances.fr','s')        : 'travail/rh_performances',
             ('@sta-portage.com','s')          : 'travail/sta_portage',
             ('jobs@itjobboard.nl','s')        : 'travail/ItJobBoard',
             ('theitjobboard.com','s')         : 'travail/ItJobBoard',
             ('@theunixjobboard.com','s')      : 'travail/ItJobBoard',
             ('recrutement@','s')              : 'travail/Divers',
             ('@evolutic.com','s')             : 'travail/Evolutic',
             ('careerbuilder.(com|fr)','m')    : 'travail/CareerBuilder',
             ('@email.pagepersonnelle.fr','s')  : 'travail/pagepersonnel',
             ('@email.pagepersonnel','s')       : 'travail/pagepersonnel',
             ('@pagepersonnel.fr>','s')         : 'travail/pagepersonnel',
             ('madison33@hotmail.com','s')     : 'pub/Toptural',
             ('correo@elporma.com','s')        : 'pub/Toptural',
             ('(lacasitadeluz|ana_compludo|lacasadelmonte)@hotmail.com','m'): 'pub/Toptural',

             ('@synchrone-technologies.fr','s'): 'travail/SynchroneTechnologies',
             ('louis.lafond@societe-portage.fr','s') : 'travail/suspect',
             ('@opteamis.com','s')             : 'travail/opteamis',
             ('recruitment@engie.(com|fr)','m'): 'travail/Angie',
             ('@idppmail.com','s')             : 'travail/IdppMail',
             ('@gft.com','s')                  : 'travail/Gft',
             ('pierre_blandin@hotmail.com','s'): 'formation/pierre_blandin',
             ('greta-massy.com','s')           : 'formation/greta_massy',
             ('patrice.andlauer@club-internet.fr','s') : 'formation/greta_massy',
             ('denis.robert4@wanadoo.fr','s')          : 'formation/greta_massy',
	     ('dquach@free.fr','s')                    : 'formation/greta_massy',
	     ('patrice.andlauer@club-internet.fr','s') : 'formation/greta_massy',
	     ('abdelkrimbouzidi@aol.com','s')          : 'formation/greta_massy',
	     ('jack_fontange@yahoo.fr','s')            : 'formation/greta_massy',
	     ('jm.beaubreuil@tele2.fr','s')            : 'formation/greta_massy',
	     ('david.sauvagnargues@free.fr','s')       : 'formation/greta_massy',
 	     ('phil.swi@orange.fr','s')                : 'formation/greta_massy',
 	     ('alsta@free.fr','s')                     : 'formation/greta_massy',
 	     ('mustapha.m@wanadoo.fr','s')             : 'formation/greta_massy',
 	     ('rolland_f@hotmail.com','s')             : 'formation/greta_massy',
 	     ('bruno.taupiac@laposte.net','s')         : 'formation/greta_massy',
              ('serge.briand@atosorigin.com','s'): 'serge_briand',
              ('@guarani.fr','s')               : 'Guarani',
              ('@blablacar.(fr|com)','m')       : 'Blablacar',
              ('@covoiturage.fr','s')           : 'Blablacar',
              ('@mailengine','s')               : 'Blablacar',
              ('farnell.com','s')               : 'fournisseurs/Farnell',
              ('conrad','s')                    : 'fournisseurs/Conrad',
              ('@radiospares.fr','s')           : 'fournisseurs/RadioSpares',
              ('rs-components.com','s')         : 'fournisseurs/RadioSpares',
              ('chr0no post','s')               : 'fournisseurs/ChronoPost',
              ('@corp.ovh.com','s')             : 'fournisseurs/Ovh',
              ('@selectronic.fr','s')           : 'fournisseurs/Selectronic',
              ('pagesjaunes.fr','s')            : 'fournisseurs/PageJaunes',
              ('(no-?reply|support|newsletter|event)@ovh.com','m') : 'fournisseurs/Ovh',
              ('lemarois@mandrakesoft.com','s') : 'cons/lemarois',
              ('lemarois@mandriva.com','s')     : 'cons/lemarois',
              ('kpmg.fr>','s')                  : 'Kpmg',
              ('@ldlc.com','s')                 : 'LDLC',
              ('aliexpress.com','s')            : 'AliExpress',
              ('direct.hiscox.fr','s')          : 'Hiscox',
              ('@hiscoxpro.fr','s')             : 'Hiscox',
              ('infos@sevigne.com','s')         : 'Hiscox',
              ('@placedesreseaux.com','s')      : 'spam/PlaceDesReseaux',
              ('@jobintree.com','s')            : 'spam/Infospratique',
              ('@infospratiques-','s')          : 'spam/Infospratique',
              ('@(supermontreete|uberpahma|ujnwret|vloaruad).net','m') : 'spam/Spam',
              ('amazon@toshaw.chimchim.org','s'): 'spam/Spam',
              ('maxi-bazar.eu','s')             : 'spam/Spam',
              ('yes_you_can_reply@guesttoguest.com','s') : 'spam/Spam',
              ('uros.+educationalist@hotmail.com','m') : 'spam/Spam',
              ('@twago.fr','s')                 : 'spam/Twago',
              ('uroc','s')                      : 'spam/Uroc',
              ('@sexydoo.com','s')              : 'spam/sexydoo',
              ('@droa.com','s')                 : 'spam/droa',
              ('nicolas georges','s')           : 'contact/NicolasGeorges',
              ('@conceptware.lu','s')           : 'societe/conceptware',
              ('@netlitiges.fr','s')            : 'forum/net_litiges',
              ('@@scienceamusante.net','s')     : 'forum/science_amusante',
              ('@art-chimie-online.com','s')    : 'forum/ArtChimie',
              ('@eevblog.com','s')              : 'forum/eev',
              ('@archlinux.fr','s')             : 'forum/ArchLinux',
              ('@phonandroid.com','s')          : 'forum/phonandroid',
              ('@compta-online.com','s')        : 'forum/comptaOnline',
              ('sfoursac@altelog.com','s')      : 'contact/StephaneFoursac',
              ('@electrolab.fr','s')            : 'contact/electrolab',
              ('@ncr.com','s')                  : 'contact/NCR',
              ('rando92@wanadoo.fr','s')        : 'reseaux_sociaux/rando92',
              ('alibaba.com','s')               : 'Alibaba',
              ('@ca-illeetvilaine.fr','s')      : 'banque/ca_iv/ca_iv',
              ('agricole-illeetvilaine.fr>','s') : 'banque/ca_iv/ca_iv',
              ('[@\.]ebay.(fr|de|com)','m')     : 'Ebay',
              ('ebay pro','s')                  : 'Ebay',
              ('sixt.fr>','s')                  : 'pub/Sixt',
              ('@hitheq.net','s')               : 'pub/cdiscount',
              ('fnac.com','s')                  : 'pub/Fnac',
              ('seloger.com','s')               : 'pub/SeLoger',
              ('infopromotions','s')            : 'pub/Infopromotions',
              ('gautier-girard.com','s')        : 'pub/GautierGirard',
              ('@mmdfrance.fr','s')             : 'pub/MmdFrance',
              ('guide comparateur','s')         : 'pub/Pub',
              ('@e-eni.com','s')                : 'pub/Pub',
              ('information2.france@hp.com','s'): 'pub/Hp',
              ('dossierfamilial.com>','s')      : 'pub/DossierFamillial',
              ('@net-iris.fr','s')              : 'pub/netIris',
              ('auchandirect','s')              : 'pub/auchant_direct',
              ('acycle','s')                    : 'pub/acycle',
              ('atmel.com','s')                 : 'pub/Atmel',
              ('gfi.fr','s')                    : 'pub/gfi',
              ('canalplay.com>','s')            : 'pub/CanalPlay',
              ('cadeautheque','s')              : 'pub/Cadeautheque',
              ('@mindmanager.fr','s')           : 'pub/mindmanager',
              ('@toucanvacances.','s')          : 'pub/toucanvacances',
              ('rentabilisez.com','s')          : 'pub/rentabilisez',
              ('(studyrama|vocatis)','m')       : 'pub/studyrama',
              ('priceminister.com','s')         : 'pub/priceminister',
              ('@priceletter.com','s')          : 'pub/priceminister',
              ('solutions linux','s')           : 'pub/SolLinux',
              ('cabestan.com','s')              : 'pub/SolLinux',
              ('@borland.com','s')              : 'pub/borland',
              ('paypal','s')                    : 'pub/paypal',
              ('@musicme.com','s')              : 'pub/MusicMe',
              ('@idvroom.com','s')              : 'pub/EasyCovoiturage',
              ('societe-portage.fr','s')        : 'pub/societe-portage', 
              ('@amazon.fr','s')                : 'pub/Amazon',
              ('@toprural.com','s')             : 'pub/toprural',
              ('@cogidata.fr','s')              : 'travail/Cogidata',
              ('sybase.com','s')                : 'pub/Sybase',
              ('traildeparis','s')              : 'pub/TrailDeParis',
              ('@appartager.com','s')           : 'pub/aparteger',
              ('alain.coron','s')               : 'contact/AlainCoron',
              ('@ville-viroflay.fr','s')        : 'contact/VilleViroflay',
              ('@france-gestion.fr','s')        : 'contact/FranceGestion',
              ('Dominique Desorbaix','s')       : 'contact/DominiqueDesorbais', 
              ('conso-one','s')                 : 'spam/Spam',
              ('@info.cine-news.fr','s')        : 'spam/Spam',
              ('webechangiste@free.fr','s')     : 'spam/Spam',
              ('webechangiste.fr','s')          : 'spam/Spam',
              ('@edesirs.com','s')              : 'spam/Spam',
              ('@yara.com','s')                 : 'spam/Spam',
              ('easyvoyage','s')                : 'spam/Spam',
              ('electroniques@mailing-infoexpo.com','s') : 'pub/Electronique',
              ('@infopalmaresduweb.com','s')    : 'spap/Spam',
              ('mailing-[0-9]?@(offres-du-jour|mail(ing)?-information|information-(mail|du-jour)).com','m') :'spam/Mailing',
              ('mesopinions.com','s')           : 'politique/MesOpinions',
              ('@liberation(\.cccampaigns)?\.(net|fr)','m') : 'politique/libe', 
              ('@collectifpsychiatrie.fr','s')  : 'politique/NuitSecuritaire',
              ('bellaciao.org','s')             : 'politique/bellaciao',
              ('@votez[0-9]{4}','m')            : 'politique/votez',
              ('[@\.]planetanoo.com','m')       : 'politique/planetanoo',
              ('@petitionpublique.fr','s')      : 'politique/Petition', 
              ('@cmonvote.com','s')             : 'politique/CmonVote',
              ('ryad@karar.fr','s')             : 'karar',
              ('@basecamp.com','s')             : 'karar',
              ('placelibertine@free.fr','s')    : 'spam/placelibertine',
              ('placelibertine.com','s')        : 'spam/placelibertine',
              ('drnmode@aol.com','s')           : 'Drnmode',
              ('@freetelecom.fr','s')           : 'FreeTelecom',
              ('@free-mobile.fr','s')           : 'Freemobile',
              ('ca-paris(mailing)?.fr','m')     : 'banque/ca_paris/ca_paris',
              ('infosclient@ceisame.fr','s')    : 'Ceisame/ceisame',
              ('facteur[0-9]+@postoffice[0-9]+-dfactory.com','m') : 'Ceisame/pub',
              ('samuelesenaro@yahoo.co.uk','s') : 'FormationDU',
              ('chaoyi.hu@gmail.com','s')       : 'proprietaire/chaoyi',
              ('immobiliere-valenciennoise@wanadoo.fr','s') : 'proprietaire/AnneSophieBraye',
              ('veroniquep@wanadoo.fr','s')     : 'reseaux_sociaux/LaMaiZon',
              ('etreville@aaescp-eap.net','s')  : 'reseaux_sociaux/LaMaiZon',
              ('la-couarde-atlantik@wanadoo.fr','s') : 'reseaux_sociaux/LaMaiZon',
              ('[@\.]peuplade.(fr|net)','m')    : 'reseaux_sociaux/Peuplade',
              ('Covoiturage.com','s')           : 'reseaux_sociaux/covoiturage_com',
              ('@sortirsurparis.net','s')       : 'reseaux_sociaux/SortirSurParis',
              ('@ratp.fr','s')                  : 'ratp',
              ('velizymodsept@free.fr','s')     : 'ml/velizymodsept',
              ('velizymodsept-request@ml.free.fr','s') : 'ml/velizymodsept',
              ('@leboncoin.fr','s')             : 'achats/le_bon_coin',
              ('voyages-sncf.com>','s')         : 'achats/voyages_sncf',
              ('@houra.fr','s')                 : 'achats/houra',
              ('@loz-production','s')           : 'achats/loz_production',
              ('@oz-live.com','s')              : 'achats/loz_production',
              ('@quickpartitions.com','s')      : 'achats/quick_partitions',
              ('@le-lion.be','s')               : 'achats/droguerie_le_lion',
              ('@mcmaster.com','s')             : 'achats/mc_master_carr',
              ('cdiscount.com>','s')            : 'achats/Cdiscount',
              ('cdiscount@servicenotification.net','s') : 'achats/Cdiscount',
              ('@discount','s')                 : 'achats/Cdiscount',
              ('@rswww.com','s')                : 'achats/Livreurs',
              ('@coffeesoft.fr','s')            : 'achats/CoffeeSoft',
              ('coffeesoft.+cdiscount','m')     : 'achats/CoffeeSoft',
              ('@oteraaulnoy.com','s')          : 'achats/Otera',
              ('@openrunner.com','s')           : 'reseaux_sociaux/openrunner',
              ('@nexity.fr','s')                : 'logement/Nexity',
              ('pad@saint-amand-les-eaux.fr','s'): 'point_acces_droits',
              ('@assistance.free.fr','s')               : 'FreeFR/assistance',
              ('hautdebit@freetelecom.fr','s')          : 'FreeFR/factures',
              ('@e-cciparisidf.fr','s')                 : 'travail/CCI_Versailles',
              ('postmaster@free.fr','s')                : 'FreeFR/postmaster',
              ('@mediatheque-st-amand.com','s')         : 'st_amand/mediatheque',
              ('sandrine.durandiere@free.fr','s')       : 'sandrine_durandiere',
              ('samouche_gliem@hotmail.com>','s')       : 'samenta_gliem',
              ('hubert.daniel@atosorigin.com>','s')     : 'hubert_daniel',
              ('pamela.wattebled@ext.vallourec.com>','s') : 'pamela_watterbled',
              ('@(info\.)?(dreamteam-portage|groupe-freeteam)\.com>','m') : 'travail/dreamteam',
              ('@inops.fr>','s' )                        : 'travail/INOPS',
              ('caf.fr>','s')                            : 'CAF',
              ('@bdl-saintamand.fr>','s')                : 'BDL_COMPTABILITE',
              ('lise.sarpaux@laposte.net>','s')          : 'lise_sarpaux',
              ('@hays\.(fr|com)>','m')                   : 'travail/hays',
              ('@laram-info.fr>','s')                    : 'LA_RAM',
              ('@abylsen.com>','s')                      : 'travail/albylsen',
              ('@ants.gouv.fr>','s')                     : 'titres_securises_gouv',
              ('@franceconnect.gouv.fr>','s')            : 'franceconnect_gouv',
              ('.service-public.fr','s')    :                  'service_public',
              ('@OUI.sncf>','s') : 'OUI_sncf',
              ('@yousign.fr>','s') : 'Signatures',
              ('@hr-team.net>','s' ) : 'travail/hr_team'

}
