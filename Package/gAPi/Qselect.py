debug = False
class Quality:
  def quality(quality1, url, u_choice):
    qualiindex=['(HDP-mp4)','(360P-mp4)','(480P-mp4)','(720P-mp4)','(1080P-mp4)']
    def Append_list(url, **a):
      Available = {}
      for num in range(len(url)):
        urlt = url[num]
        key = urlt.text.replace(' ','').replace('Download','').strip()
        if (key not in qualiindex):
          break
        subkey = urlt.find('a')['href']
        Available[f"link_{num}"] = {}
        Available[f"link_{num}"]['Quality'] = key
        Available[f"link_{num}"]['Link'] = subkey
      if a:
        return(len(Available))
      return(Available)
    def Textinator(url):
      return(url.text.replace(' ', '').replace('Download', '').strip())
    def process_dict(data):
      quality = data['Quality']
      link = data['Link']
      return(quality, link)
    modified = False
    confine = False
    if quality1 == "BEST":
      print(f">>Preffered: {qualiindex[0]}")
      #Same mechanic, different method
      if Append_list(url)[f"link_0"]["Quality"] == qualiindex[0]:
        print(f">>Found: {qualiindex[0]}")
        return (url[0],qualiindex[0])
      else:
        if u_choice == "manual":
          print("HDP not found")
         # print('NO QUALITY MATCHED')
          print('--Manual Selection--')
          line = []
          name = []
          for num in range(0,5):
            listed = url[num].text.replace(' ', '').replace('Download', '').strip()
            name.append(listed)
            if listed not in qualiindex:
              break
            line.append(url[num])
            print(f'{num+1}.) {listed}')
          while True:
            keyword = input('Select quality:')
            try:
              keyword = (int(keyword)-1)
              if keyword > (num-1):
                continue
              elif keyword <= 0:
                continue
              else:
                selected = line[keyword]
                qual = name[keyword]
                print(f">>Selected: {qual}")
                return(selected, qual)
            except BaseException as e:
              print(e)
              continue
        else:
          print("HDP not found")
          v_y = (Append_list(url, a=True) - 1)
          test_value = 5
          while True:
            ##Go Lower quality
            if v_y == 0:
              test_value -= 1
              v_y = (Append_list(url, a=True) - 1)
            #Check for the highest Quality possible
            try:
              if Append_list(url)[f"link_{v_y}"]:
              #Dictionary exist then check if its the highest possible value
                if Append_list(url)[f"link_{v_y}"]["Quality"] == qualiindex[test_value]:
                  selected = Append_list(url)[f'link_{v_y}']
                  processed_qual, processed_link = process_dict(selected)
                  found = selected["Quality"]
                  dictionary_link = {"href" : processed_link}
                  print(f">>Adjusted to: {found}")
                  return(dictionary_link, processed_qual)
                else:
                  v_y -= 1
            except IndexError:
              v_y -= 1
    
    else:
      quality = f"({quality1}-mp4)"
      print(f">>Preffered: {quality}")
    if quality == qualiindex[4]:
      y=4
      qual = qualiindex[4]
    elif quality == qualiindex[3]:
      y=3
      qual = qualiindex[3]
    elif quality == qualiindex[2]:
      y=2
      qual = qualiindex[2]
    elif quality == qualiindex[1]:
      y=1
      qual = qualiindex[1]
    if u_choice == "auto":
      t = 0
      while True:
        t += 1
        if t == 10:
          print(f"[{t}]TimeOut")
          print(f">>Adjusted to: {qualiindex[0]}")
          return (url[0],qualiindex[0])
          continue
        try:
          v_y = (Append_list(url, a=True) - 1)
          while True:
            selected = Append_list(url)[f'link_{v_y}']
            processed_qual, processed_link = process_dict(selected)
            if processed_qual != qualiindex[y]:
              v_y -= 1
              continue
            break
              #raise KeyError('Adjust the quality')
            
        except KeyError as error:
          if debug == True:
            print(error)
          modified = True
          if y == 1 and not confine:
            y += 1
            confine=True
          elif confine:
            y += 1 
            if y == 4:
              y = 0
          elif y == 4:
            y = 0
          else:
            y -= 1
          continue
        if processed_qual == qualiindex[y]:
          qual = processed_qual
          if modified:
            print(f">>Adjusted to: {qual}")
          else:
            print(f">>Found: {qual}")
          dictionary_link = {"href" : processed_link}
          return(dictionary_link, qual)
    else:
      try:
        selected = url[y]
        if Textinator(selected) in qualiindex:
          print(f">>Found: {qual}")
          return(selected, qual)
        else:
          raise KeyError("Find another quality")
      except KeyError:
        modified = True
        print('NO QUALITY MATCHED')
        print('--Manual Selection--')
        line = []
        name = []
        for num in range(0,5):
          listed = url[num].text.replace(' ', '').replace('Download', '').strip()
          name.append(listed)
          if listed not in qualiindex:
            break
          line.append(url[num])
          print(f'{num+1}.) {listed}')
        while True:
          keyword = input('Select quality:')
          try:
            keyword = (int(keyword)-1)
            if keyword > (num-1):
              continue
            elif keyword <= 0:
              continue
            else:
              selected = line[keyword]
              qual = name[keyword]
              print(f">>Selected: {qual}")
              return(selected, qual)
          except BaseException as e:
            print(e)
            continue

        
    #if experimental=true:
      #code
      
      