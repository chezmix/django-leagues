from django.db import models
from django.contrib import admin

# Import our custom widget and our model from where they're defined
from django_leagues.models import Player, League, Season, Match, MatchResult


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name')
    fields = ('user',)
    
    
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'player_list')
    fields = ('name', 'players')


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'league', 'started', 'player_list')
    fields = ('name', 'league', 'players', 'started')

    
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_date', 'season', 'player_list')
    fields = ('match_date','season', 'players')
    
class MatchResultAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'match', 'score')
    
    # TODO: Revisit this
    fields = ('player', 'match', 'score')


admin.site.register(Player, PlayerAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(MatchResult, MatchResultAdmin)
