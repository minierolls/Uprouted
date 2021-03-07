import requests
import json
import polyline

api_key = ""

# Get current location coordinates
geo_r = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key={}".format(api_key)).json()
curr_latitude = geo_r["location"]["lat"]
curr_longitude = geo_r["location"]["lng"]
mode = "walking"
radius = "500"

# Get list of nearby places within radius
latitude = "40.444229"
longitude = "-79.943367" # CMU coordinates
nearby_r = requests.post("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&key={}".format(latitude, longitude, radius, api_key)).json()

# Finding directions to nearby places
for place in nearby_r["results"][:1]:
    dest = place["place_id"]
    r = requests.post("https://maps.googleapis.com/maps/api/directions/json?origin={},{}&destination=place_id:{}&key={}&mode={}".format(latitude, longitude, dest, api_key, mode))
    print(r.text)

# Turning returned polyline into list of coordinates
pline = "asimEjawnUD~@RRjGUb@TRf@@pFCbCuIDGZzICHGHiAF{HKk@QO{@_@wA@_DXQSCw@?g@_@?yH@aTBcDTkGVgGCcBm@_A}@a@u@}A_Do@k@uCq@{BYgBBgEb@sG`B_Br@kA\\s@QyCeAkBa@wA?qA^gHbG}EdE}@nAeCtBuFxFaGpGwMtNaChCaChDeBlDiAdD}ApGcDxU}@hEmAxD}[tt@wOv]wH~MgBhD_DzHqM~[kIrSaLxWmF|KcD`FkKrNaDfF{@pB}@~CkBfJiEfRgBbG{DzJmCnFuFpJgGxLeKvU}Rtc@aLbW{DbHsCxDqDpDiD~DaAvA{BnDaAzAiCtEeEbKcA`DwEdNuDlJ_IrQgBdE}DjJiDnGuDdHsCvG}AzDwDvHeEtJsJ~UeJvTwBrFaK|TkG`MwM`XuNn[gHvOsE|HyGrJeEzE{I~IwIrIiJ~JqAjBeD`GuFtLcExHuHnKsGxGcH`F_MxHuJdGaa@tV{JbGgItFoI`GmNxIaRzKkJnFy]lSyb@zVyDlCsClC}GlJka@pn@wSv[oAbBmDnDuGdEsAj@oKjCaO|CyLlCqFxBeCtAwJ|GoFrDeGzFcPbPqOtOwBdCaDhFkDvF{AhBkCpCem@lk@{FbFsJrFqAv@cFjEcNfMgHbHkMlO_EbGmBtD}BlDiCxCwF`Fs@p@iDdEoAxBoBjFaAlC}Kx[qDvPmBrEsB`EaFtNoIlV}@hD_AzFk@~I?v]?rTMdD_@jEu@vEgAbEqGvRoKz[eFrPCt@k@hCkAdE}JrY{HdUmEfKaChEqClDqFzEqDrBkEbA}BNuA?cD]cDOaDLsFDeFo@wJw@kPNkDZuDl@mEpAsEnB}IrDaC~BcAzBe@zBg@fH{Cp]gAhSFzIWzB]zAaCjF{CtFqLpTkFhIaGzGkP|MuCpCyEfHiF|HqFhJoCfHeCrJmJj_@eK|ZwBbHoChIoC`HeD|LkGb\\iB~K_CpPoBhPcBrKgAlEiAzCeCxFuQpe@oEfIyC`FkKnPeDpDgDjC}MhH}FhDyBvBuAnBcG~KmErHgBbCmE|DeCbBqNfHiEtBeDrBaBzAcBxBiCdGcArFYnGG`Ha@bF{@zDkBnEyCxFwLbVsGxLaDpDkD~BqFfB{YlGgEx@aDhAyGhDwFlEeEzEsIlKqE|EuJhGmFnFs@v@_A~@wAdAmA`A{@v@oCbCcE~BmAx@wBpB{AhCg@h@iAbA_ArAWA_@I}@k@cA]_AO}AEY?"
res = polyline.decode(pline, geojson=True)
