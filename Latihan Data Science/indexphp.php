<?php
function tambah($a,$b){
    $c = $a + $b;
    if ($c < 100){
        echo ("Maaf Saldo Anda Belum Cukup : ".$c);
    }
    else{
        echo ("Selamat Saldo Anda Cukup : ".$c);
    };
    return $c;
};

function kurang($a,$b){
    $c = $a - $b;
    if ($c < 100){
        echo ("Maaf Saldo Anda Belum Cukup : ".$c);
    }
    else{
        echo ("Selamat Saldo Anda Cukup : ".$c);
    };

    return $c;
};

function kali($a,$b){
    $c = $a * $b;
    if ($c < 100){
        echo ("Maaf Saldo Anda Belum Cukup : ".$c);
    }
    else{
        echo ("Selamat Saldo Anda Cukup : ".$c);
    };

    return $c;
};

function bagi($a,$b){
    $c = $a / $b;
    if ($c < 100){
        echo ("Maaf Saldo Anda Belum Cukup : ".$c);
    }
    else{
        echo ("Selamat Saldo Anda Cukup : ".$c);
    };
    return $c;
};

function hitung_umur($tanggal_lahir){
	$birthDate = new DateTime($tanggal_lahir);
	$today = new DateTime("today");
	if ($birthDate > $today) { 
	    exit("0 tahun 0 bulan 0 hari");
	}
	$y = $today->diff($birthDate)->y;
	$m = $today->diff($birthDate)->m;
	$d = $today->diff($birthDate)->d;
	return $y." tahun ".$m." bulan ".$d." hari";
}

function fibonachi(){
    $angka_sebelumnya=0;
    $angka_sekarang=1;
    
    //tampilkan 2 angka awal
    echo "$angka_sebelumnya"."<br>". $angka_sekarang."<br>";

    for ($i=0; $i<25; $i++)
    {
    // hitung angka yang akan ditampilkan
    $output = $angka_sekarang + $angka_sebelumnya;
    echo " $output";
    //siapkan angka untuk perhitungan berikutnya
    $angka_sebelumnya = $angka_sekarang;
    $angka_sekarang = $output;
    }
}

function listwarna(){
    $a = "yellow";

    switch($a){
        case "hijau" : 
                    echo ("Warna ini adalah hijau");
                    break;
        case "merah" :
                    echo ("Warna ini adalah merah");
                    break;
        default  :
                    echo ("Warna Anda tidak ada!!!");

    }
}

echo("Kalkulator Sederhana<br>");
echo("==================<br>");
echo tambah(2,5)."<br>";
echo kurang(100,3)."<br>";
echo kali(120400,100000)."<br>";
echo bagi(1000,3)."<br>";
echo ("Hitung Umur <br>");
echo ("Umur Anda Saat Inni Adalah : ".hitung_umur("1990-09-01")."<br>");
echo fibonachi()."<br>";
echo listwarna();
?>