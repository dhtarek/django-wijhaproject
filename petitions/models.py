from django.db import models

# Create your models here.
SPEC = (
    ('Logement public locatif','Logement public locatif'),
    ('Aide de l’Etat pour le logement rural','Aide de l’Etat pour le logement rural'),
    ('Lotissements immobilières sociales','Lotissements immobilières sociales'),
    ('Logement promotionnel aidé','Logement promotionnel aidé'),
    ('Logement de fonction','Logement de fonction'),
    ('Désistement logement public','Désistement logement public'),
    ('Dotation en eau potable','Dotation en eau potable'),
    ('Raccordement au réseau du gaz','Raccordement au réseau du gaz'),
    ('Raccordement au réseau électrique','Raccordement au réseau électrique'),
    ("Raccordement au réseau public d’assainissement",'Raccordement au réseau public d’assainissement'),
    ('Eclairage public','Eclairage public'),
    ('Aménagement des voies publiques','Aménagement des voies publiques'),
    ('Aménagement urbain','Aménagement urbain'),
    ('collecte des déchets ménagers','collecte des déchets ménagers'),
    ('Réalisation des établissements de santé de proximité','Réalisation des établissements de santé de proximité'),
    ('Réalisation des établissements scolaires','Réalisation des établissements scolaires'),
    ('Réalisation de bureaux de poste','Réalisation de bureaux de poste'),
    ('Réalisation des annexes administratives','Réalisation des annexes administratives'),
    ('Réalisation des aires de sport','Réalisation des aires de sport'),
    ('Réalisation des aires de loisirs','Réalisation des aires de loisirs'),
    ('Réalisation des centres culturels','Réalisation des centres culturels'),
    ('Réalisation des centres de sureté urbaine','Réalisation des centres de sureté urbaine'),
    ('Expropriation pour cause d’utilité publique','Expropriation pour cause d’utilité publique'),
    ('Atteinte à la propriété foncière','Atteinte à la propriété foncière'),
    ('Permis de construire','Permis de construire'),
    ('Permis de démolir','Permis de démolir'),
    ('Régularisation de la situation juridique du foncier','Régularisation de la situation juridique du foncier'),
    ('Mise en conformité des constructions dans la cadre de la loi n° 08-15','Mise en conformité des constructions dans la cadre de la loi n° 08-15'),
    ('Demandes d’emploi','Demandes d’emploi'),
    ('Réintégration professionnelle (emploi)','Réintégration professionnelle (emploi)'),
    ('Demande de transfer (emploi)','Demande de transfer (emploi)'),
    ('Recours (emploi)','Recours (emploi)'),
('Investissement Industriel','Investissement Industriel'),
    ('Investissement Agricole','Investissement Agricole'),
    ('Investissement Prestation de services','Investissement Prestation de services'),
    ('Pensions et allocations','Pensions et allocations'),
    ('Aides sociales','Aides sociales'),
('Cantines scolaires','Cantines scolaires'),
    ('Transport scolaire','Transport scolaire'),
    ('chauffage scolaire','chauffage scolaire'),
    ('Aménagement des écoles','Aménagement des écoles'),
    ('Contrats et marchés publics','Contrats et marchés publics'),
('Activités commerciales et économiques','Activités commerciales et économiques'),
    ('Culture et loisirs','Culture et loisirs'),
    ('Activité agricole','Activité agricole'),
    ('Santé','Santé'),
    ('Transport','Transport'),
('Activités règlementées','Activités règlementées'),
    ('Etat civil','Etat civil'),
    ('Demandes d’audience','Demandes d’audience'),
    
)


class petitions (models.Model):
    Num_enr = models.IntegerField(default = 0 )
    date_declaration= models.DateTimeField(auto_now=False)
    num_cit = models.IntegerField()
    specialite = models.CharField(max_length=500,choices=SPEC)
    object = models.TextField(max_length = 1000)
    finish = models.BooleanField(default=False)
    code_req = models.CharField(max_length=250)
    num_domaine = models.IntegerField()
    num_com = models.IntegerField()
    agent = models.CharField( max_length=50)

    def __str__(self):
        return self.Num_enr

    
