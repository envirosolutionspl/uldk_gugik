# ULDK


## PL

 Wtyczka QGIS, która pozwala na pobieranie geometrii granic działek katastralnych, obrębów, gmin, powiatów i województw wraz z atrybutami. Pobieranie danych jest realizowane przez usługę ULDK udostępnianą przez Główny Urząd Geodezji i Kartografii.

## Instrukcja pobrania
1. Wtyczkę należy zainstalować w QGISie jako ZIP bądź wgrać pliki wtyczki do lokalizacji C:\Users\User\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins.
2. Aby uruchomić wtyczkę należy kliknąć na ikonę zielonego drzewa oznaczonego napisem ULDK.
3. Jeżeli ikona wtyczki nie jest widoczna w panelu warstw, spróbuj zrestartować QGIS.
4. Jeżeli wtyczka nadal nie jest widoczna  należy przejść w QGIS Desktop do Wtyczki -> Zarządzanie wtyczkami -> Zainstalowane -> ULDK -> Odinstalować wtyczkę, i zainstalować ponownie.<br>
## Instrukcja użytkowania: 

### Wybór sposobu wyszukiwania i pobrania obrysu:
 Wtyczka posiada 3 sposoby wyszukiwania i pobierania obrysu.

 * Zakładka pierwsza - <b>Wybór przez ID</b><br>
    Sposobem pierwszym możemy pobrać interesujący nas obiekt lub obszar przez podanie jego numeru TERYT np. dla działki: <b>WWPPGG_R.XXXX.NDZ</b> lub <b>WWPPGG_R.XXXX.AR_NR.NDZ</b> gdzie:
   - "WW" to kod województwa
   - "PP" to kod powiatu
   - "GG" to kod gminy
   - "R" to cyfra określająca typ gminy (np. 1-gmina miejsca, 2- gmina wiejska...)
   - "XXXX" to numer ewidencyjny obrębu ewidencyjnego, z zakresem od 0001 do 9999
   - "NDZ"  to  numer ewidencyjny działki 
   - "AR_NR" to numer arkusza mapy ewidencyjnej, gdzie "NR" to numer porządkowy tego arkusza
 
 * Zakładka druga - <b>Wybór przez współrzędne</b><br> 
    Drugim sposobem można wyszukać interesujący nas obiekt na podstawie określenia jego współrzędnych oraz układu, w którym się one znajdują lub wybraniu go bezpośrednio na mapie (skrót ALT+F).
    Po wciśnięciu kombinacji ALT+F kursor zmieni się w krzyżyk, w tym momencie możemy wybrać obszar do pobrania.<br>
    <b>Pamiętaj: Pobierany jest obszar zaznaczony w oknie wtyczki.</b>

 * Zakładka trzecia - <b>Wybór obiektu przez nazwę obrębu i numer działki</b><br>
   W celu wyszukania działki ewidencyjnej należy wybrać z listy kolejno województwo, powiat, gminę oraz obręb, a następnie wprowadzić nr działki.
   Jeżeli obiekt znajduje się na więcej niż jednym z arkuszy, konieczy będzie wybór tego, z którego chcemy pobrać.

   W bocznym panelu znajdują się pola wyboru obszaru, który nas interesuje (działka, obręb, gmina, powiat, województwo).
   Jeżeli chcemy pobrać warstwę województwa, w którym przykładowo znajduje się nasza działka należy zaznaczyć w bocznym panelu "Województwo". 
   Mając wpisany identyfikator działki wtyczka automatycznie pobierze przypisane do niej województwo lub inny wybrany obszar.
   Jeśli numer działki występuje więcej niż jeden raz w danym obrębie, w górnej części QGIS’a pojawi się komunikat i zostanie pobrana pierwsza z działek zwrócona przez usługę ULDK.

### Uwaga

Warunkiem koniecznym do prawidłowego działania wtyczki jest posiadanie wersji QGIS 3.16.16 lub wyższej.



# ULDK

## EN

A QGIS plugin that allows you to download the geometry of cadastral parcels, land districts, municipalities, counties, and voivodeships. Data retrieval is carried out through the ULDK service provided by the Main Office of Geodesy and Cartography.

## Download Instructions
1. Install the plugin in QGIS as a ZIP file or upload the plugin files to the following location: C:\Users\User\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins.
2. To run the plugin, click on the icon of a green tree labeled "ULDK."
3. If the plugin icon is not visible in the layer panel, try restarting QGIS.
4. If the plugin is still not visible, go to QGIS Desktop, select Plugins -> Manage Plugins -> Installed -> ULDK -> Uninstall the plugin, and then reinstall it.

## Usage Instructions:

### Choosing the Method of Searching and Downloading Boundaries:
The plugin offers 3 methods for searching and downloading boundaries.

* Tab 1 - **Wybór przez ID**<br>
   In the first method, you can download the object or area of interest by providing its TERYT number, e.g., for a land parcel: **WWPPGG_R.XXXX.NDZ** or **WWPPGG_R.XXXX.AR_NR.NDZ**, where:
   - "WW" is the voivodeship code.
   - "PP" is the county code.
   - "GG" is the municipality code.
   - "R" is the digit indicating the type of municipality (e.g., 1-municipal, 2-rural municipality...).
   - "XXXX" is the registration number of the registration area, ranging from 0001 to 9999.
   - "NDZ" is the registration number of the parcel.
   - "AR_NR" is the number of the cadastral map sheet, where "NR" is the sequential number of that sheet.

* Tab 2 - **Wybór przez współrzędne**<br>
   The second method allows you to search for an object of interest based on its coordinates and the coordinate system in which they are located, or select it directly on the map (shortcut ALT+F). After pressing ALT+F, the cursor will change to a crosshair, and at this    point, you can select the area to download.<br>
   <b>Remember: The area selected in the plugin window will be downloaded.</b>

* Tab 3 - **Wybór obiektu przez nazwę obrębu i numer działki**<br>
   To search for a parcel, select the voivodeship, county, municipality, and registration area from the list, and then enter the parcel number. If the object is located on more than one of the sheets, you will need to choose which one to download.

In the side panel, there are options to select the area of interest (parcel, registration area, municipality, county, voivodeship). If you want to download the voivodeship layer where your parcel is located, select "Województwo" in the side panel. Once you enter the parcel identifier, the plugin will automatically download the associated voivodeship or another selected area. If the parcel number appears more than once in the same registration area, a message will appear at the top of QGIS, and the plugin will download the first parcel returned by the ULDK service.

### Note
A necessary condition for the plugin to work correctly is having QGIS version 3.16.16 or higher."
