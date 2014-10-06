Assignment One:
https://github.com/ga-students/DS_BOS_04/wiki/Assignment-1

* For setting up Lahman Baseball statistics in Postgres 
credit: https://github.com/brentnycum/lahman-postgres

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>playerid</th>
      <th>awardid</th>
      <th>yearid</th>
      <th>lgid</th>
      <th>tie</th>
      <th>notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0 </th>
      <td>  bondto01</td>
      <td> Pitching Triple Crown</td>
      <td> 1877</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>1 </th>
      <td> hinespa01</td>
      <td>          Triple Crown</td>
      <td> 1878</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>2 </th>
      <td> heckegu01</td>
      <td> Pitching Triple Crown</td>
      <td> 1884</td>
      <td> AA</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>3 </th>
      <td> radboch01</td>
      <td> Pitching Triple Crown</td>
      <td> 1884</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>4 </th>
      <td> oneilti01</td>
      <td>          Triple Crown</td>
      <td> 1887</td>
      <td> AA</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>5 </th>
      <td> keefeti01</td>
      <td> Pitching Triple Crown</td>
      <td> 1888</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>6 </th>
      <td> clarkjo01</td>
      <td> Pitching Triple Crown</td>
      <td> 1889</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>7 </th>
      <td> rusieam01</td>
      <td> Pitching Triple Crown</td>
      <td> 1894</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>8 </th>
      <td> duffyhu01</td>
      <td>          Triple Crown</td>
      <td> 1894</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>9 </th>
      <td> youngcy01</td>
      <td> Pitching Triple Crown</td>
      <td> 1901</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>10</th>
      <td> lajoina01</td>
      <td>          Triple Crown</td>
      <td> 1901</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>11</th>
      <td> wadderu01</td>
      <td> Pitching Triple Crown</td>
      <td> 1905</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>12</th>
      <td> mathech01</td>
      <td> Pitching Triple Crown</td>
      <td> 1905</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>13</th>
      <td> mathech01</td>
      <td> Pitching Triple Crown</td>
      <td> 1908</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>14</th>
      <td>  cobbty01</td>
      <td>          Triple Crown</td>
      <td> 1909</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>15</th>
      <td> johnswa01</td>
      <td> Pitching Triple Crown</td>
      <td> 1913</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>16</th>
      <td> alexape01</td>
      <td> Pitching Triple Crown</td>
      <td> 1915</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>17</th>
      <td> alexape01</td>
      <td> Pitching Triple Crown</td>
      <td> 1916</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>18</th>
      <td> johnswa01</td>
      <td> Pitching Triple Crown</td>
      <td> 1918</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>19</th>
      <td> vaughhi01</td>
      <td> Pitching Triple Crown</td>
      <td> 1918</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>20</th>
      <td> alexape01</td>
      <td> Pitching Triple Crown</td>
      <td> 1920</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>21</th>
      <td> hornsro01</td>
      <td>          Triple Crown</td>
      <td> 1922</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>22</th>
      <td> johnswa01</td>
      <td> Pitching Triple Crown</td>
      <td> 1924</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>23</th>
      <td> vanceda01</td>
      <td> Pitching Triple Crown</td>
      <td> 1924</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>24</th>
      <td> hornsro01</td>
      <td>          Triple Crown</td>
      <td> 1925</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>25</th>
      <td> grovele01</td>
      <td> Pitching Triple Crown</td>
      <td> 1930</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>26</th>
      <td> grovele01</td>
      <td> Pitching Triple Crown</td>
      <td> 1931</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>27</th>
      <td>  foxxji01</td>
      <td>          Triple Crown</td>
      <td> 1933</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>28</th>
      <td> kleinch01</td>
      <td>          Triple Crown</td>
      <td> 1933</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>29</th>
      <td> gomezle01</td>
      <td> Pitching Triple Crown</td>
      <td> 1934</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>30</th>
      <td> gehrilo01</td>
      <td>          Triple Crown</td>
      <td> 1934</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>31</th>
      <td> gomezle01</td>
      <td> Pitching Triple Crown</td>
      <td> 1937</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>32</th>
      <td> medwijo01</td>
      <td>          Triple Crown</td>
      <td> 1937</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>33</th>
      <td> waltebu01</td>
      <td> Pitching Triple Crown</td>
      <td> 1939</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>34</th>
      <td> fellebo01</td>
      <td> Pitching Triple Crown</td>
      <td> 1940</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>35</th>
      <td> willite01</td>
      <td>          Triple Crown</td>
      <td> 1942</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>36</th>
      <td> newhoha01</td>
      <td> Pitching Triple Crown</td>
      <td> 1945</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>37</th>
      <td> willite01</td>
      <td>          Triple Crown</td>
      <td> 1947</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>38</th>
      <td> mantlmi01</td>
      <td>          Triple Crown</td>
      <td> 1956</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>39</th>
      <td> koufasa01</td>
      <td> Pitching Triple Crown</td>
      <td> 1963</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>40</th>
      <td> koufasa01</td>
      <td> Pitching Triple Crown</td>
      <td> 1965</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>41</th>
      <td> koufasa01</td>
      <td> Pitching Triple Crown</td>
      <td> 1966</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>42</th>
      <td> robinfr02</td>
      <td>          Triple Crown</td>
      <td> 1966</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>43</th>
      <td> yastrca01</td>
      <td>          Triple Crown</td>
      <td> 1967</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>44</th>
      <td> carltst01</td>
      <td> Pitching Triple Crown</td>
      <td> 1972</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>45</th>
      <td> goodedw01</td>
      <td> Pitching Triple Crown</td>
      <td> 1985</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>46</th>
      <td> clemero02</td>
      <td> Pitching Triple Crown</td>
      <td> 1997</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>47</th>
      <td> clemero02</td>
      <td> Pitching Triple Crown</td>
      <td> 1998</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>48</th>
      <td> martipe02</td>
      <td> Pitching Triple Crown</td>
      <td> 1999</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>49</th>
      <td> johnsra05</td>
      <td> Pitching Triple Crown</td>
      <td> 2002</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>50</th>
      <td> santajo01</td>
      <td> Pitching Triple Crown</td>
      <td> 2006</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>51</th>
      <td> peavyja01</td>
      <td> Pitching Triple Crown</td>
      <td> 2007</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>52</th>
      <td> verlaju01</td>
      <td> Pitching Triple Crown</td>
      <td> 2011</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>53</th>
      <td> kershcl01</td>
      <td> Pitching Triple Crown</td>
      <td> 2011</td>
      <td> NL</td>
      <td> None</td>
      <td> None</td>
    </tr>
    <tr>
      <th>54</th>
      <td> cabremi01</td>
      <td>          Triple Crown</td>
      <td> 2012</td>
      <td> AL</td>
      <td> None</td>
      <td> None</td>
    </tr>
  </tbody>
</table>

