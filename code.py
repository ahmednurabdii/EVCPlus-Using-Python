import datetime

pin = input('Fadlan geli PIN-kaaga (Enter PIN)')

if pin == "3639":
    print("1.Itus Haraaga")
    print("2.kaarka hadalka")
    print("3.Bixi Biil")
    print("4.U wareeji EVCPLus")
    print("5.Warbixin Kooban")
    print("6.Salaam Bank")
    print("7.Maareynta")
    print("8.TAAJ")
    A = int(input(print("9.BIIL Paynment")))

    if A == 1:
        print("[-EVCPlus-] Haraagaadu waa $300")
    elif A == 2:
        B = int(input(print("Kaarka hadalka\n1.ku shubo Airtime\n2.Ugu Shub Airtime\n3.MIFI Packages\n4.ku shubo Internet\n5.Ugu shub qof kale")))

        if B == 1:
            C = int(input(print("Fadlan Geli lacagta")))
            print("Ma hubtaa inaad $", C  , "ugu shubtid Undefined")
            print("1.Haa")
            y = int(input(print("2.Maya")))
            if y == 1:
                z = 300
                print("Waxaa ku shubatay $" ,C,"\nHaraagaadu waa",z-C)
            elif y == 2:
                print("Fadlan kusoo noqo markale")

        if B == 2:
            D = int(input(print("Fadlan Geli Mobileka")))
            E = int(input(print("Fadlan Geli lacagta")))
            print("Ma hubtaa inaad $", D, "ugu shubtid ",E)
            print("1.Haa")
            F = int(input(print("2.Maya")))
            if F == 1:
                Z = 300
                print("Waxaa Ugu shubtay $",E, "lambarka",D, "\nHaraagaadu waa $",Z-E)
            elif F == 2:
                print("Fadlan kusoo noqo markale")

        if B == 3:
            G = int(input(print("1.ku shubo Data-da MIFI")))
            if G == 1:
                I = int(input(print("--Internet Bundle Recharge--\n1.Maalinle(Daily\n2.Isbuucle(Weekly)\n3.Bile(Monthly")))
                if I == 1:
                    J = int(input(print("Fdalan dooro bundle ka\n1.$1 = 2GB\n2.$2 = 5GB")))
                    K = int(input(print("Fdalan Gali MIFI user")))
                    L = int(input(print("Ma hubtaa inaad$",J,"ugu shubto",K,"\n1.Haa\n2.Maya")))
                    if L == 1:
                        X = 3J-1
                        Z = 300
                        print("Waxaa Ugu shubtay $",J, "MIFI USER", K,f"\nwaxaana heshay Data  ", 3*J - 1,"GB \nHaraagadu EVCplus waa $",Z-J)
                    elif L == 2:
                        print("Fadlan kusoo noqo markale")
                elif I == 2:
                    M = int(input(print("Fdalan dooro bundle ka\n1.$5 = 10GB\n2.$10 = 25GB")))
                    N = int(input(print("Fdalan Gali MIFI user")))
                    O = int(input(print("Ma hubtaa inaad$", 5*M, "ugu shubto", N, "\n1.Haa\n2.Maya")))
                    if O == 1:
                            X = 3J - 1
                            Z = 300
                            print("Waxaa Ugu shubtay $", 5*M, "MIFI USER", N, f"\nwaxaana heshay Data  ", 15 * M - 5,
                                  "GB \nHaraagadu EVCplus waa $", Z - M*5)
                    elif O == 2:
                            print("Fadlan kusoo noqo markale")
                elif I == 3:
                    M = int(input(print("Fdalan dooro bundle ka\n1.$20 = 40GB\n2.$40 = 85GB\n3.$60 = 150GB")))
                    N = int(input(print("Fdalan Gali MIFI user")))
                    O = int(input(print("Ma hubtaa inaad$", 20 * M, "ugu shubto", N, "\n1.Haa\n2.Maya")))
                    if O == 1:
                            X = 3J - 1
                            Z = 300
                            print("Waxaa Ugu shubtay $", 20 * M, "MIFI USER", N, f"\nwaxaana heshay Data  ", 45 * M - 5,
                                    "GB \nHaraagadu EVCplus waa $", Z - M * 20)
                    elif O == 2:
                            print("Fadlan kusoo noqo markale")


    elif A == 3:
        C = int(input(print("BIXI BIIL \n1.Post Paid\n2.Ku iibso")))
        if C == 1:
                x = int(input(print("Post Paid\n1.Ogow Biilka\n2.Bixi Biil\n3.Ka Bixi Biil")))
                if x == 1:
                    print("Error occurred, please try again later :iima furmo cml: ")
                elif x == 2:
                    N = int(input(print("Fdalan Gali lacagta")))
                    Y = int(input(print("ma hubtaa inaaad bixisid biilka lacagtiisu tahay: $",N,"?\n1 HAA\n2 Maya")))
                    if Y == 1:
                        z = 300
                        print("waxaad Bixisay Biil ahaan udirtay $",N,"?\nHraagadu waa ",z-A)
                    elif Y == 2:
                        print("Haraaga xisaabta kuguma filna")
                elif x == 3:
                    V = int(input(print("Fdalan Gali Mobile-ka")))
                    A = int(input(print("Fdalan Gali lacagta")))
                    P = int(input(print("ma hubtaa inaaad bixisid biilka lacagtiisu tahay: $", A, "oo laga rabo tel NO",V,"?\n1 HAA\n2 Maya")))
                    if P == 1:
                        z = 300
                        print("waxaad Bixisay Biil ahaan udirtay $", A,"oo laga rabo tel NO",V,"?\nHaraagadu waa ",z-A )
                    elif P == 2:
                        print("Fadlan kusoo noqo markale")
        elif C == 2:
            V = int(input(print("Fdalan Gali aqoonsiga ganacsiga")))
            print("parter doesnt not exist")
    elif A == 4:
        Q = int(input(print("Fdalan Gali Mobile-ka")))
        P = int(input(print("Fadlan Gali Lacagta")))
        N = int(input(print("Ma hubtaa inaad $",P,"u wareejisid ",Q,"\n1. HAA\n2. MAYA")))
        if N == 1:
            Z = 300
            print("{EVCPLus} waxaad $",P,"u wareejisid",Q,"\nHaraagadu waa $",Z-P)
        elif N == 2:
            print("Ku soo noqo fadlan mahadsanid")
    elif A == 5:
        D = int(input(print("Warbixin Kooban\n1.Last Action\n2.Wareejintii U dambeysay\n3.iibsashadii U dambeysay\n4.Last 3 Actions\n5.Email Me My Activity")))
        if D == 1:
            time = datetime.datetime.now()
            print("$23 Ayaad ka heshay 25261XXXXXXX, Taariikh:",time)
        elif D == 2:
            S = int(input(print("Statementiga\n1.U dirtay\n2.kaheshay")))
            if S == 1:
                R = int(input(print("Fadlan Geli Mobile-ka")))
                print("Your mini statement has been sent as SMS to your registered mobile No")
            elif S == 2:
                H = int(input(print("Fadlan Geli Mobile-ka")))
                print("Your mini statement has been sent as SMS to your registered mobile No")
            elif S == 3:
                U = int(input(print("Fadlan Geli aqoonsiga Ganacsiga")))
                print("operation succeded\nNo Transaction to display!")
            elif S == 4:
                AA = int(input(print("Your mini statement has been sen as SMS to your mobile NO")))
            elif S == 5:
                AB = int(input(print("Fadlan Geli Emial kaaga")))
                print("operation success full")

    elif A == 6:
        AC = int(input(print("1.Ka wareeji EVCPlus")))
        AD = int(input(print("Fadlan door xisaabta Bangiga\n1.SALAAM SOMALI BANK\n2.salaam Sch")))
        if AD == 1:
            AE = int(input(print("Fadlan Geli Account-ka")))
            AF = int(input(print("Fadlan Geli macluumaad")))
            print("kuuma furna")
        elif AD == 2:
            AG = int(input(print("Fadlan Geli Account-ka")))
            AH = int(input(print("Fadlan Geli macluumaad")))
            print("kuuma furna")

    elif A == 7:
        AG = int(input(print("Maareynta\n1.Bedel lambarka sirta ah\n2.Bedel luqadda\n3.wargelin Mobile Lumay\n4.Lacag Xirasho\n5.U celi lacag qaldantay\n6.EnableMobileBanking")))
        if AG == 1:
            AHH = int(input(print("Fadlan Geli PIN-kaaga cusub")))
            AHA = int(input(print("Hubi PIN-kaaga cusub")))
            print("Waala badalay PIN-kaaga")

    elif A== 8:
        AG = int(input(print("TAAJ\n1.Dibada\n2.Ogoow Khidmada\n3.Mcluumadka xawaalada")))
        if AG == 1:
            Agg = int(input(print("Fadlan Geli faleefan qaataha")))
            Ag = int(input(print("Fadlan Geli magaca qaataha")))
            AHg = int(input(print("Fadlan Geli magaalada qaataha joogo")))
            Agh = int(input(print("Fadlan Geli lacagta")))
            AHH = int(input(print("Fadlan ma hubtaa in aad ",Ag,"oo jooga wadanka",AHg,"lambarkisuna yahay",Agg,"in aad udireesid $",Agh,"mahubtaa\n1.Haa\n2.Maya")))
            if AHH == 1:
                Z = 300
                print("waxaad udirtay",Ag,"oo lambarkisu yahay ",Agg,"joogana wadanka",AHg,"lacagta aad udirtay waa $",Agh,"haraagadu waa ",Z-Agh)
            elif AHH == 2:
                print("Fadlan Markale kusoo noqo mahadsanid")

        if AG == 2:
            Aaa = int(input(print("Fadlan dooro\n1.PAY TO EVCPlus\n2.TAAJ\n3.TaajPay\n4.New Etaaj\n5.TAAJ IPS")))
            if Aaa == 1:
                Aba = int(input(print("Fadlan gali Taleefanka qaataha")))
                Aca = int(input(print("Fadlan gali lacagta")))
                Ada = int(input(print("ma hubtaa inaad udirtay ",Aba,"lacag dhan $",Aca,"\n1.Haa\n2.Maya")))
                if Ada == 1:
                    Z = 300
                    print("waxaad udirtya aacounka ah ",Aba,"lacagdhan $",Aca,"\nHaraagadu waa ",Z-Aca)
                elif Ada == 2:
                    print("Fadlan Markale kusoo noqo mahadsanid")

            elif Aaa == 2:
                Aab = int(input(print("Fadlan gali Taleefanka qaataha")))
                Aac = int(input(print("Fadlan gali lacagta")))
                Aad = int(input(print("ma hubtaa inaad udirtay ", Aab, "lacag dhan $", Aac, "\n1.Haa\n2.Maya")))
                if Aad == 1:
                    Z = 300
                    print("waxaad udirtya aacounka ah ", Aab, "lacagdhan $", Aac, "\nHaraagadu waa ", Z - Aac)
                elif Aad == 2:
                    print("Fadlan Markale kusoo noqo mahadsanid")

            elif Aaa == 3:
                Abb = int(input(print("Fadlan gali aqoonsiga lacag diridda")))
                print("misssing")

    elif A == 9:
        AAB = int(input(print("EVCPlus\n1.itus Haraaga Bill ka\n2.Wada bixi biil-ka\n3.Qayb ka bixi Biil-ka")))
        if AAB == 1:
            ABB = int(input(print("Fadlan gali billka Reference number")))
            print("haraagadu waa $ 200")
        elif AAB == 2:
            ABC = int(input(print("Fadlan gali billka Reference number")))
            print("invalid ")
        elif AAB == 3:
            ABD = int(input(print("Fadlan gali billka Reference number")))
            print("pls kuuma furno TAAJ")





else:
    print("PINKAGA waa qalad")
