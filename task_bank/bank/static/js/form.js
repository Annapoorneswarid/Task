
    function populate(s1,s2)
    {
    var s1=document.getElementById(s1);
    var s2= document.getElementById(s2);
    s2.innerHTML="";


    if(s1.value =="1")
    {
    var optionArray=['Chengannur|Chengannur', 'Cherthala|Cherthala', 'Kayamkulam|Kayamkulam', 'Haripad|Haripad', 'Mavelikara|Mavelikara'];

    }
    else if (s1.value == '2')
    {
    var optionArray=['Muvattupuzha|Muvattupuzha', 'Aluva|Aluva', 'Kakkanad|Kakkanad'];
    }
    else if (s1.value == '3')
    {
    var optionArray=['Thodupuzha|Thodupuzha', 'Kattappana|Kattappana'];
    }
    else if (s1.value == '4')
    {
    var optionArray=['Ancharakkandy|Ancharakkandy', 'Perumpadavu|Perumpadavu', 'Paisakary|Paisakary', 'Thalassery|Thalassery'];
    }
    else if (s1.value == '5')
    {
    var optionArray=['Paduppu|Paduppu', 'Kanhangad|Kanhangad','Nileshwaram|Nileshwaram'];
    }
    else if (s1.value == '6')
    {
    var optionArray=['Kottarakkara|Kottarakkara', 'Pallimukku|Pallimukku'];
    }else if (s1.value == '7')
    {
    var optionArray=['Erumely|Erumely', 'Kanjirappally|Kanjirappally','Manarcad|Manarcad'];
    }else if (s1.value == '8')
    {
    var optionArray=['Thamarassery|Thamarassery', 'Vadakara|Vadakara','Koyilandy|Koyilandy'];
    }
    else if (s1.value == '9')
    {
    var optionArray=['Thirunavaya|Thirunavaya', 'Ponnani|Ponnani','Kottakkal|Kottakkal'];
    }else if (s1.value == '10')
    {
    var optionArray=['Pathiripala|Pathiripala', 'Cheruplassery|Cheruplassery','Ottapalam|Ottapalam'];
    }else if (s1.value == '11')
    {
    var optionArray=['Adoor|Adoor', 'Konni|Konni'];
    }
    else if (s1.value == '12')
    {
    var optionArray=['Meluliyazhathara|Meluliyazhathara', 'Kallambalam|Kallambalam','Varkala|Varkala'];
    }else if (s1.value == '13')
    {
    var optionArray=['Koratty|Koratty', 'Triprayar|Triprayar','Paluvai|Paluvai','Guruvayur|Guruvayur'];
    }else if (s1.value == '14')
    {
    var optionArray=['Meppady|Meppady', 'Panamaram|Panamaram'];
    }




    for(var option in optionArray)
    {
    var pair = optionArray[option].split("|");
    var newoption = document.createElement("option");

    newoption.value = pair[0];
    newoption.innerHTML=pair[1];
    s2.options.add(newoption);
    }
    }

