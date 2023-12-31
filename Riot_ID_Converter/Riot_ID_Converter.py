import pyperclip

def user_input():
    user_input = input("Type N to exclude alts. Otherwise press enter: ")
    return user_input

def riot_id_converter(riot_id_table, include_alts):
    #copies from clipboard
    input_text = pyperclip.paste()
    output_lines = []

    for line in input_text.split('\n'):
        modified_line = line.strip()

        #users with custom RIOT ID tag
        for riot_id, suffix_list in riot_id_table.items():
            
            if riot_id in line:
                #includes only the main account of the users
                if include_alts == 'N':
                    modified_line = suffix_list[0]
                
                #include all the accounts of the users
                else:
                    modified_line = '\n'.join(suffix_list)
                
                output_lines.append(modified_line)
                break
                    
        #users without a custom RIOT ID tag        
        else:
            modified_line += '#NA1'
            modified_line = modified_line[3:] 
            if modified_line and modified_line[0].isspace():
                modified_line = modified_line[2:]
            output_lines.append(modified_line)
            
        
    #saves to clipboard
    output_text = '\n'.join(output_lines)
    pyperclip.copy(output_text)

#add new usernames here
riot_id_table = {
    'Acetize': ['Acetize#Ace'
                ],
    'Akudama': ['Akudama#TGA'
                ],
    'Alucard': ['Alucard#sun'
                ],
    'aquanick': ['aquanick#BBCSR'
                 ],
    'arskapupu': ['arskapupu#FIN'
                  ],
    'Àrtemıs': ['Artemis#KSJP'
                ],
    'Auracle': ['Solarreta#moon'
                ],
    'baby princess': ['baby princess#hime',
                      '姐姐的貓#pet'
                      ],
    'Baerus': ['Baerus#001',
               ],
    'BANANA CREAM': ['hide on meds#1010'
                     ],
    'bbnomoola': ['bbnomoola#gravy'
                  ],
    'Buffing': ['Buffing#0001'
                ],
    'ceiko': ['ceiko#mwah'
              ],
    'ChampBl': ['zzz#Nik'
                ],
    'CircasLoL': ['Circas#1876' ,
                ],
    'Cloudjumper': ['Cloudjumper#CYDRA'
                    ],
    'Corvus1': ['Corvus Crow#666',
                ],
    'Crab Degenerate': ['Crab Degenerate#CRAB'
                        ],
    'Danman fan 96': ['Marius#Aya',
                      'きえたい#1798'
                      ],
    'Devi': ['Rena#Mei', 
             ],
    'Dûnk': ['Dunk#NA2'
             ],
    'EVERYBODYKILLER': ['prodigy zzz#NA1',
                        'EVERYBODYKILLER#NA1'
                        ],
    'Exile Syre': ['Syre#Exile'
                   ],
    'goat of rakan': ['emanex#0519'
                      ],
    'hallucinate': ['hallucinate#xo'
                    ],
    'Her Boba': ['Her Boba#ily'
                 ],
    'Hoppermh': ['Hoppermh#NA1',
                 'Galaxy Kitty#NA1'
                 ],
    'Imaginarium': ['neverlamb#bei'
                    ],
    'in time': ['in time#0313',
                ],
    'Irelia101': ['Rezzy#101'
                  ],
    'Irghaos': ['Irghaos#1738'
                ],
    'jckliu': ['jck#NA1'
               ],
    'JustBran': ['Justbran#BLM'
                 ],
    'Kayle King': ['Aim ツ#Bot'
                   ],
    'King Kazi': ['Kazi#1999'
                  ],
    'Km1er Fan': ['Weakside midlane#Meow'
                  ],
    'LiterallyPotatoe': ['LiterallyPotatoe#tato'
                         ],
    'l3lue': ['Blue#UU70',
              ],
    'Maso': ['Maso#rita'
             ],
    'Matarra': ['Matarra#sad'
                ],
    'MrJimmyOG': ['MrJimmyOG#NA1',
                  'Mrjimmyog#Glurp'
                  ],
    'Neco arcc': ['Tower Of God#Bam',
                  ],
    'Pibly': ['pibly#0000'
              ],
    'PropertyOfDrew': ['PropertyOfDrew#00000',
                       ],
    'remove assassins': ['Gio#2576'
                         ],
    'Rockabananza': ['Rockabananza#0001'
                     ],
    'ryginltga': ['ryginltga#NA1',
                  'Hash#BBC',
                  #'Hashtag#NA2'
                  ], 
    'Rezzy': ['Rezzy#101'
              ],
    'Richard Socks ON': ['C Tier Fill#Socks'
                         ],
    'rohan': ['rohan#9999'
              ],
    'R0YSH': ['K M#0666',
              ],
    'Samba': ['Samba#555'
              ],
    'Sated': ['Sated#YASUO'
              ],
    'Shin Reisurodo': ['福生玄黄天尊#0001',
                       'Tama#0777'
                       ],
    'Slainy': ['Slain#NA2'
               ],
    'Slimere': ['Slimere#BBC'
                ],
    'Sokeri EUW xD': ['skrillexdubbstep#edm',
                      ],
    'SOVEREIGN444': ['Sovereign#BLM'
                     ],
    'Stollen': ['Stollen#00000'
                ],
    'Suyeonchan': ['Suyeonchan#00000',
                   ],
    'SWAGMASTER83': ['SWAGMASTER83#FATFK'
                     ],
    'Teal Frost': ['thai tea#4444'
                   ],
    'TeamGiveMeC': ['downr#cncr',
                    ],
    'Theworldisunfair': ['volumedown#444'
                         ],
    'The Noxian': ['counter#Noxus'
                   ],
    'The y45h': ['y45hthed0ng3r#y45h'
                 ],
    'thigh high sIut': ['dopamine#vice',
                        ],
    'ThisGameIsJoever': ['ThisGameIsJoever#2319'
                         ],
    'TSM GnomeSlayer': ['Pulbarizer Fan#NA1'
                        ],
    'USC jjking': ['土黑娃 #NA300'
                   ],
    'Vicky': ['Lil Rave Bae#0000'
              ],
    'xDeer': ['Deer#123'
              ],
    'yukito6': ['yukito6#Yuki'
                ],
    'Yunì': ['Yunì#9864'
             ],
    'Zavøky': ['Zav#777',
               'zzzgzGGGgjgRr532#NA1'
               ],
    'Z 4': ['Z 4#CLAP'
            ],
    '545': ['Pulbarizer Fan#RNG',
            #'big c#rng'
            ],
}

include_alts = user_input()

riot_id_converter(riot_id_table, include_alts)
