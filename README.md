# ULDK

PL: Wtyczka QGIS, która pozwala na pobieranie geometrii granic działek katastralnych, obrębów, gmin, powiatów i województw. Pobieranie danych jest realizowane przez usługę ULDK udostępnianą przez Główny Urząd Geodezji i Kartografii.

## PL

 Wtyczka QGIS, która pozwala na pobieranie geometrii granic działek katastralnych, obrębów, gmin, powiatów i województw. Pobieranie danych jest realizowane przez usługę ULDK udostępnianą przez Główny Urząd Geodezji i Kartografii.

## Instrukcja pobrania
1. Wtyczkę należy zainstalować w QGISie jako ZIP bądź wgrać pliki wtyczki do lokalizacji C:\Users\User\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins.
2. Aby uruchomić wtyczkę należy kliknąć na ikonę zielonego drzewa oznaczonego napisem ULDK
3. Jeżeli ikona wtyczki nie jest widoczna w panelu warstw, spróbuj zrestartować QGIS.
4. Jeżeli wtyczka nadal nie jest widoczna  należy przejść w QGIS Desktop do Wtyczki -> Zarządzanie wtyczkami -> Zainstalowane -> ULDK -> Odinstalować wtyczkę, i zainstalować ponownie.

## Instrukcja użytkowania: 

## Wybór sposobu wyszukiwania i pobrania obrysu:
 Wtyczka posiada 3 sposoby wyszukiwania i pobierania obrysu.

 * Zakładka pierwsza - <b>Wybór przez ID</b>
    Sposobem pierwszym możemy pobrać interesujący nas obiekt lub obszar przez podanie jego numeru TERYT np. dla działki: <b>WWPPGG_R.XXXX.NDZ</b>  ,gdzie:
   - "WW" to kod województwa
   - "PP" to kod powiatu
   - "GG" to kod gminy
   - "R" to cyfra określająca typ gminy (np. 1-gmina miejsca, 2- gmina wiejska...)
   - "XXXX" to numer ewidencyjny obrębu ewidencyjnego, z zakresem od 0001 do 9999
   - "NDZ"  to  numer ewidencyjny działki 
   - "AR_NR" to numer arkusza mapy ewidencyjnej, gdzie "NR" to numer porządkowy tego arkusza


   W bocznym panelu znajdują się pola wyboru obszaru, która nas interesuje (działka, obręb, gmina, powiat, województwo)
   Jeżeli chcemy pobrać warstwę województwa w którym przykładowo znajduje się nasza działka należy zaznaczyć w bocznym panelu "Województwo". 
   Mając wpisany identyfikator działki wtyczka automatycznie pobierze przypisane do niej województwo lub inny wybrany obszar.
   Jeśli numer działki występuje na więcej niż jednym z arkuszy, udzielona zostanie informacja zwrotna.
 
 * Zakładka druga - <b>Wybór przez współrzędne</b> 
    Drugim sposobem można wyszukać, pobrać interesujący nas punkt na podstawie określenia jego współrzędnych oraz układu, w którym się one znajdują lub wybraniu go bezpośrednio na mapie (skrót ALT+D)
    Po wciśnięciu kombinacji ALT+D kursor zmieni się w krzyżyk, w tym momencie możemy wybrać obszar do pobrania.
    Pamiętaj: Pobierany jest obszar zaznaczony w oknie wtyczki.

 * Zakładka trzecia - <b>Wybór obiektu przez nazwę województwa</b>
   Należy dokonać wyboru obszaru, który należy pobrać zaczynając od województwa.
   Z tego poziomu również dostępna jest opcja pobrania województwa, obszaru czy powiatu, do którego przypisana jest działka.
   Dużym plusem tego sposobu jest to, że określając wszystkie parametry działki, jest dostępny również podgląd na arkusze, na których znajduje się działka o podanym numerze.

### Uwaga

Warunkiem koniecznym do prawidłowego działania wtyczki jest posiadanie wersji QGIS (tu wpisać wersję) lub wyższej.



## EN

 The plugin allows user to download geometry of parcells, communies, regions. Plugin uses ULDK API of The Central Office of Geodesy and Cartography of Poland;

## Installation Instructions
1. To install the plugin, you should either install it as a ZIP file in QGIS or upload the plugin files to the following location: C:\Users\User\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins.
2. To run the plugin, click on the icon of a green tree labeled "ULDK."
3. If the plugin icon is not visible in the layers panel, try resetting QGIS.
4. If the plugin is still not visible, go to QGIS Desktop, then to Plugins -> Manage and Install Plugins -> Installed -> ULDK -> Uninstall the plugin, and reinstall it.

## User Guide
## Choosing the Search and Download Method:
The plugin offers three ways to search and download geometrical data.

* First tab - <b>Selection by ID</b>
   The first method allows you to download the object or area of interest by providing its ID. For example, for a parcel: <b>WWPPGG_R.XXXX.NDZ</b>, where:

   - "WW" is the province code.
   - "PP" is the county code.
   - "GG" is the commune code.
   - "R" is a digit indicating the type of commune (e.g., 1 for a city commune, 2 for a rural commune...).
   - "XXXX" is the numerical identifier of the registration area, ranging from 0001 to 9999.
   - "NDZ" indicates the numerical identifier of the parcel.
   - "AR_NR" is the number of the registration map sheet, where "NR" is the ordinal number of the sheet.

   In the side panel, you will find fields to select the area of interest (parcel, registration area, commune, county, province). If you want to download the province layer in which your parcel is located, select "Province" in the side panel. With the parcel identifier entered, the plugin will automatically download the associated province or another selected area. If the parcel number exists on multiple sheets, you will receive feedback.

* Second tab - <b>Selection by Coordinates</b>
   The second method allows you to search for and download a specific point based on its coordinates and the coordinate system in which it is located. You can also select a point directly on the map (shortcut ALT+D). After pressing ALT+D, the cursor will change to a crosshair, and at that moment, you can choose the area to download. Please note that the downloaded area will be the one selected in the plugin window.

* Third tab - <b>Selection by Object Name of the Province</b>
   You should select the area you want to download, starting from the province. From this level, you can also download the province, area, or county to which the parcel is assigned. A significant advantage of this method is that by specifying all the parcel parameters, you can also view the sheets on which the parcel with the given number is located.

### Note
A prerequisite for the correct operation of the plugin is having QGIS version (insert version) or higher.


