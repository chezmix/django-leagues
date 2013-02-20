from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User)
    
    def full_name(self):
        return self.user.first_name + " " + self.user.last_name
        
    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name



class League(models.Model):
    name = models.CharField(max_length=200)
    players = models.ManyToManyField(Player)
    
    def __unicode__(self):
        return self.name
     
    def player_list(self):
        players_in_this_league = self.players.all()
        return ", ".join([player.user.first_name for player in players_in_this_league])


class Season(models.Model):
    name = models.CharField(max_length=200)
    league = models.ForeignKey(League) 
    players = models.ManyToManyField(Player)
    
    started = models.BooleanField()
    
    def player_list(self):
        players_in_this_season = self.players.all()
        return ", ".join([player.user.first_name for player in players_in_this_season])
        
    def __unicode__(self):
        return self.name + " (" + self.league.name + ")"



class Match(models.Model):
    match_date = models.DateTimeField(verbose_name="Match date")
    season = models.ForeignKey(Season)
    players = models.ManyToManyField(Player)

    class Meta:
        verbose_name_plural = "matches"

    def results(self):
        pass
    
    def player_list(self):
        playing_this_match = self.players.all()
        return ", ".join([player.user.first_name for player in playing_this_match])
        
    def __unicode__(self):
        return str(self.match_date) + " (" + self.player_list() + ") " + str(self.season)


class MatchResult(models.Model):
    player = models.ForeignKey(Player)
    match = models.ForeignKey(Match)
    score = models.IntegerField()
    
    def player_name(self):
        return self.player.full_name()
