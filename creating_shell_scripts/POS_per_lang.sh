#! /bin/bash 
function POS_per_lang { 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_english.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/english_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_afrikaans.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/afrikaans_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_arabic.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/arabic_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_belarusian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/belarusian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_bulgarian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/bulgarian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_catalan.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/catalan_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_czech.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/czech_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_welsh.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/welsh_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_danish.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/danish_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_north_sami.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/north_sami_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_german.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/german_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_estonian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/estonian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_greek.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/greek_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_spanish.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/spanish_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_basque.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/basque_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_persian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/persian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_french.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/french_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_irish.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/irish_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_scottish_gaelic.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/scottish_gaelic_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_galician.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/galician_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_gothic.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/gothic_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_korean.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/korean_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_armenian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/armenian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_hindi.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/hindi_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_croatian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/croatian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_indonesian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/indonesian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_italian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/italian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_hebrew.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/hebrew_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_kazakh.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/kazakh_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_latin.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/latin_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_latvian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/latvian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_lithuanian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/lithuanian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_hungarian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/hungarian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_maltese.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/maltese_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_marathi.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/marathi_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_dutch.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/dutch_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_japanese.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/japanese_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_polish.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/polish_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_portuguese.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/portuguese_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_romanian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/romanian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_russian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/russian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_sanskrit.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/sanskrit_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_slovak.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/slovak_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_slovenian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/slovenian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_serbian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/serbian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_finnish.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/finnish_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_swedish.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/swedish_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_tamil.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/tamil_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_telugu.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/telugu_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_turkish.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/turkish_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_ukrainian.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/ukrainian_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_urdu.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/urdu_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_uyghur.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/uyghur_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_vietnamese.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/vietnamese_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_classical_chinese.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/classical_chinese_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_wolof.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/wolof_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_chinese.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/chinese_POS.txt 
grep -v $'#' joined_by_lang/data_joined_by_lang/all_old_church_slavonic.conllu | grep . | awk '{print $4}' | sort | uniq -c | sort -nr >>joined_by_lang/results_joined_by_lang/old_church_slavonic_POS.txt 
} 
POS_per_lang