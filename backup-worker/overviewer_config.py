worlds["survival"] = "/tmp/backup/world"

renders["survivalday"] = {
    "world": "survival",
    "title": "Survival Daytime",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
}

renders["survivalnight"] = {
    "world": "survival",
    "title": "Survival Nighttime",
    "rendermode": smooth_night,
    "dimension": "overworld",
}

end_lighting = [Base(), EdgeLines(), Lighting(strength=0.5)]
end_smooth_lighting = [Base(), EdgeLines(), SmoothLighting(strength=0.5)]

renders["End"] = {
    "world": "survival",
    "title": "Survival End",
    "rendermode": end_smooth_lighting,
    "dimension": "end",
}
#
#renders["survivalnethersouth"] = {
#    "world": "survival",
#    "title": "Survival Nether",
#    "rendermode": nether_smooth_lighting,
#    "dimension": "nether",
#    "northdirection" : "lower-right",
#}

#renders["creative"] = {
#    "world": "creative",
#    "title": "Creative",
#    "rendermode": smooth_lighting,
#    "dimension": "overworld",
#}

outputdir = "/webmap"
texturepath = "/root/.minecraft/versions/1.17/1.17.jar"
processes=2
