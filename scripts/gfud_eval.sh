#! /bin/bash
function gfud_eval {

    gfud eval macro LAS gold_standard/simplified/simple_Russia_english_gold_standard.conllu gold_standard/simplified/simple_Russia_english_intro_UDPipe.conllu >> results_gfud/gfudeval.txt ;
    echo >> results_gfud/gfudeval.txt ;
    gfud eval micro LAS gold_standard/simplified/simple_Russia_english_gold_standard.conllu gold_standard/simplified/simple_Russia_english_intro_UDPipe.conllu >> results_gfud/gfudeval.txt ;
    echo >> results_gfud/gfudeval.txt ;
    gfud eval macro UAS gold_standard/simplified/simple_Russia_english_gold_standard.conllu gold_standard/simplified/simple_Russia_english_intro_UDPipe.conllu >> results_gfud/gfudeval.txt ;
    echo >> results_gfud/gfudeval.txt ;
    gfud eval micro UAS gold_standard/simplified/simple_Russia_english_gold_standard.conllu gold_standard/simplified/simple_Russia_english_intro_UDPipe.conllu >> results_gfud/gfudeval.txt ;
    echo >> results_gfud/gfudeval.txt ;

    gfud eval macro LAS gold_standard/simplified/simple_Russia_spanish_gold_standard.conllu gold_standard/simplified/simple_Russia_spanish_intro_UDPipe.conllu >> results_gfud/gfudeval.txt ;
    echo >> results_gfud/gfudeval.txt ;
    gfud eval micro LAS gold_standard/simplified/simple_Russia_spanish_gold_standard.conllu gold_standard/simplified/simple_Russia_spanish_intro_UDPipe.conllu >> results_gfud/gfudeval.txt ;
    echo >> results_gfud/gfudeval.txt ;
    gfud eval macro UAS gold_standard/simplified/simple_Russia_spanish_gold_standard.conllu gold_standard/simplified/simple_Russia_spanish_intro_UDPipe.conllu >> results_gfud/gfudeval.txt ;
    echo >> results_gfud/gfudeval.txt ;
    gfud eval micro UAS gold_standard/simplified/simple_Russia_spanish_gold_standard.conllu gold_standard/simplified/simple_Russia_spanish_intro_UDPipe.conllu >> results_gfud/gfudeval.txt ;
    echo >> results_gfud/gfudeval.txt ;

    gfud eval macro LAS gold_standard/simplified/simple_Russia_french_gold_standard.conllu gold_standard/simplified/simple_Russia_french_intro_UDPipe.conllu >> results_gfud/gfudeval.txt ;
    echo >> results_gfud/gfudeval.txt ;
    gfud eval micro LAS gold_standard/simplified/simple_Russia_french_gold_standard.conllu gold_standard/simplified/simple_Russia_french_intro_UDPipe.conllu >> results_gfud/gfudeval.txt ;
    echo >> results_gfud/gfudeval.txt ;
    gfud eval macro UAS gold_standard/simplified/simple_Russia_french_gold_standard.conllu gold_standard/simplified/simple_Russia_french_intro_UDPipe.conllu >> results_gfud/gfudeval.txt ;
    echo >> results_gfud/gfudeval.txt ;
    gfud eval micro UAS gold_standard/simplified/simple_Russia_french_gold_standard.conllu gold_standard/simplified/simple_Russia_french_intro_UDPipe.conllu >> results_gfud/gfudeval.txt ;
    echo >> results_gfud/gfudeval.txt ;

    gfud eval macro LAS gold_standard/simplified/simple_Russia_english_gold_standard.conllu gold_standard/simplified/simple_Russia_english_intro_UDPipe.conllu units >> results_gfud/gfud_macro_las_english.txt ;
    gfud eval micro LAS gold_standard/simplified/simple_Russia_english_gold_standard.conllu gold_standard/simplified/simple_Russia_english_intro_UDPipe.conllu units >> results_gfud/gfud_micro_las_english.txt ;
    gfud eval macro UAS gold_standard/simplified/simple_Russia_english_gold_standard.conllu gold_standard/simplified/simple_Russia_english_intro_UDPipe.conllu units >> results_gfud/gfud_macro_uas_english.txt ;
    gfud eval micro UAS gold_standard/simplified/simple_Russia_english_gold_standard.conllu gold_standard/simplified/simple_Russia_english_intro_UDPipe.conllu units >> results_gfud/gfud_micro_uas_english.txt ;

    gfud eval macro LAS gold_standard/simplified/simple_Russia_spanish_gold_standard.conllu gold_standard/simplified/simple_Russia_spanish_intro_UDPipe.conllu units >> results_gfud/gfud_macro_las_spanish.txt ;
    gfud eval micro LAS gold_standard/simplified/simple_Russia_spanish_gold_standard.conllu gold_standard/simplified/simple_Russia_spanish_intro_UDPipe.conllu units >> results_gfud/gfud_micro_las_spanish.txt ;
    gfud eval macro UAS gold_standard/simplified/simple_Russia_spanish_gold_standard.conllu gold_standard/simplified/simple_Russia_spanish_intro_UDPipe.conllu units >> results_gfud/gfud_macro_uas_spanish.txt ;
    gfud eval micro UAS gold_standard/simplified/simple_Russia_spanish_gold_standard.conllu gold_standard/simplified/simple_Russia_spanish_intro_UDPipe.conllu units >> results_gfud/gfud_micro_uas_spanish.txt ;

    gfud eval macro LAS gold_standard/simplified/simple_Russia_french_gold_standard.conllu gold_standard/simplified/simple_Russia_french_intro_UDPipe.conllu units >> results_gfud/gfud_macro_las_french.txt  ;
    gfud eval micro LAS gold_standard/simplified/simple_Russia_french_gold_standard.conllu gold_standard/simplified/simple_Russia_french_intro_UDPipe.conllu units >> results_gfud/gfud_micro_las_french.txt ;
    gfud eval macro UAS gold_standard/simplified/simple_Russia_french_gold_standard.conllu gold_standard/simplified/simple_Russia_french_intro_UDPipe.conllu units >> results_gfud/gfud_macro_uas_french.txt ;
    gfud eval micro UAS gold_standard/simplified/simple_Russia_french_gold_standard.conllu gold_standard/simplified/simple_Russia_french_intro_UDPipe.conllu units >> results_gfud/gfud_micro_uas_french.txt ;

}  

gfud_eval