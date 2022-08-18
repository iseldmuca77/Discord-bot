#include<iostream>

#include<cstdlib>

#include <stdlib.h>
using namespace std;
int main(){
	int pin;
	int password = 123;
	int count=0;
	bool isTrue = true;
	double balance = 1000.0;
	int entry;
	double withdraw = 0.0;
	double deposit = 0.0;
	int gamble;
	int crime;
	int crime_random;
	string gift_gamble;
	int puna = 1;
	int puna_zgjedhja;
	
	//system("Color 4E");
	system("Color E4");
	do
	{
		cout << "***Welcome to Iseld Game***" << endl;
		cout << "Vendosni pin-in: ";
		cin >> pin;
		
		if(pin == password)
		{
			do
			{
				cout << "***Welcome to Iseld Bank***" << endl;
			    cout << "1. Depozit        2.Terhiq"<<endl;
				cout << "3. Balanca        4.Dil"<<endl;
				cout << "5. Ve bast        6.Puno"<<endl;
				cout << "7. Bej krim       8.Dhurate"<<endl;
				cout << "\n\n";
			    cout << "Zgidh nje opsion: ";
			    cin >> entry;
			    cout << endl;
			   
				
				switch(entry)
			{
				case 1:
					if(withdraw > 0.0){
					cout << "                        Sasia e lekeve te depozituara:";
					cin >> deposit;
					balance = balance + deposit;
					break;}
					else{
						cout << "Te lutem fitoni lek:\n";
						cout << "Ju mund te fitoni leke me keto opsione:\n";
						cout << "5. Ve bast        6.Puno"<<endl;
						cout << "7. Bej krim       8.Dhurate"<<endl;
						cout << "\n\n";
						break;
					}
				case 2:
					cout << "Sasi e lekeve per te terhequr:";
					cin >> withdraw;
					balance = balance - withdraw;
					break;
				case 3:
					cout << "Ju keni : " << balance << " leke ne banke!" << endl << endl;
					cout << "Ju keni : " << withdraw << " leke kesh!" << endl << endl;
					break;
				case 4:
					cout << "Mirupafshim!" << endl;
					isTrue = false;
					break;
				case 5:
					if(withdraw > 0.0){
					cout << "Iseld's gambling game:\n";
					gamble = rand() % 2 + 1;
					if(gamble==1){
						cout << "Ju fituat 100 leke\n";
						balance = balance + 100;
						cout << "Ju tani keni " << balance << " leke.\n";
						cout << endl;
					}
					else if(gamble==2){
						cout << "Ju humbet 100 leke\n";
						balance = balance - 100;
						cout << "Ju tani keni " << balance << " leke.\n";
						cout << endl;
					}
					else{
						cout << "Error 404";
					}
					break;}
					else{
						cout << "Duhet te terhiqni leke!\n";
						cout << "Sasi e lekeve per te terhequr:";
					    cin >> withdraw;
					    balance = balance - withdraw;
						break;
					}
				case 6:
					if(puna<=6){
						puna++;
						cout << "Zgjidhni nje nga punet e meposhtme:\n";
						cout << "1.Pastrues            2.Mesues\n";
						cout << "3.Mekanik             4.Inxhiner\n";
						cout << "5.DJ                  6.Doktor\n";
						cin >> puna_zgjedhja;
						switch(puna_zgjedhja){
							case 1:
									cout << "Ti zgjodhe profesionin Pastrues:\n";
									cout << "Ti sapo fitove 100 leke\n";
									balance = balance + 100;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 2:
									cout << "Ti zgjodhe profesionin Mesues:\n";
									cout << "Ti sapo fitove 200 leke\n";
									balance = balance + 200;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 3:
									cout << "Ti sapo zgjodhe profesionin Mekanik:\n";
									cout << "Ti fitove 150 leke\n";
									balance = balance + 150;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 4:
									cout << "Ti zgjodhe profesionin Inxhinier:\n";
									cout << "Ti sapo fitove 300 leke\n";
									balance = balance + 300;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 5:
									cout << "Ti sapo zgjodhe profesionin DJ:\n";
									cout << "Ti sapo fitove 500 leke\n";
									balance = balance + 500;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 6:
									cout << "Ti zgjodhe profesionin Doktor:\n";
									cout << "Ti sapo fitove 800 leke\n";
									balance = balance + 800;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
						}
						break;
					}
					else{
						cout << "Ju e keni plotesuar orarin e punes ditore:\n";
						break;
					}
					break;
				case 7:
					cout << "Zgjidhni nje nga krimet e meposhtme: " << endl;
					cout << "1.Vrasje       2.Plagosje\n";
					cout << "3.Vjedhje      4.Bullizim\n";
					cin >> crime;
					switch(crime){
						case 1:
							gamble = rand() % 5 + 1;
							switch(gamble){
								case 1:
									cout << "Ti e vrave me sukses targetin:\n";
									cout << "Ti sapo fitove 500 leke\n";
									balance = balance + 500;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 2:
									cout << "Ti e vrave me sukses targetin:\n";
									cout << "Ti sapo fitove 100 leke\n";
									balance = balance + 100;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 3:
									cout << "Ti nuk e vrave me sukses targetin:\n";
									cout << "Ti nuk fitove asnje leke\n";
									balance = balance + 0;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 4:
									cout << "Ti nuk e vrave me sukses targetin:\n";
									cout << "Ti sapo u kape nga policia dhe duhet te shlyesh 500 leke per te dale nga burgu\n";
									balance = balance - 500;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 5:
									cout << "Ti e vrave me sukses targetin:\n";
									cout << "Ti sapo fitove 300 leke\n";
									balance = balance + 300;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
							}
						break;
						case 2:
							gamble = rand() % 3 + 1;
							switch(gamble){
								case 1:
									cout << "Ti e plagose me sukses targetin:\n";
									cout << "Ti sapo fitove 250 leke\n";
									balance = balance + 250;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 2:
									cout << "Ti e plagose me sukses targetin:\n";
									cout << "Ti sapo fitove 50 leke\n";
									balance = balance + 50;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 3:
									cout << "Ti nuk e plagose targetin:\n";
									cout << "Ti nuk fitove asnje leke\n";
									balance = balance + 0;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
							}
						case 3:
							gamble = rand() % 4 + 1;
							switch(gamble){
								case 1:
									cout << "Ti vodhe me sukses targetin:\n";
									cout << "Ti sapo fitove 350 leke\n";
									balance = balance + 350;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 2:
									cout << "Ti e vodhe me sukses targetin:\n";
									cout << "Ti sapo fitove 600 leke\n";
									balance = balance + 600;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 3:
									cout << "Ti nuk e vodhe targetin:\n";
									cout << "Ti nuk fitove asnje leke\n";
									balance = balance + 0;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 4:
									cout << "Ti u kape duke vjedhur targetin:\n";
									cout << "Tani duhet te paguash 500 leke per te dale nga burgu\n";
									balance = balance - 500;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
							}
						case 4:
							gamble = rand() % 3 + 1;
							switch(gamble){
								case 1:
									cout << "Ti bullizove me sukses targetin:\n";
									cout << "Ti sapo fitove 850 leke\n";
									balance = balance + 850;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 2:
									cout << "Ti e bullizove me sukses targetin:\n";
									cout << "Ti sapo fitove 100 leke\n";
									balance = balance + 100;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
								case 3:
									cout << "Ti nuk e bullizove dot targetin:\n";
									cout << "Ti nuk fitove asnje leke\n";
									balance = balance + 0;
									cout << "Ju tani keni " << balance << " leke.\n";
								break;
							}
					}
					break;
				case 8:
					cout << "Shkruani -pleasehelp \n" << endl;
					cin >> gift_gamble;
					if(gift_gamble == "-pleasehelp"){
						gamble = rand() % 100 + 1;
						cout << "Juve sapo ju dhuruan " << gamble << "leke\n";
						balance = balance + gamble;
						cout << "Ju tani keni " << balance << " leke\n";
						break;
					}
					else{
						cout << "Error 404";
					}
			}
		
			}while(isTrue != false);
		}
	
		else
		{
			count++;
			 if(count == 3){
			 	isTrue = false;
			 }
			 else{
			 	cout << "Pin i gabuar" << endl;
			 }
		}
	}while(isTrue != false);
	return 0;
}
