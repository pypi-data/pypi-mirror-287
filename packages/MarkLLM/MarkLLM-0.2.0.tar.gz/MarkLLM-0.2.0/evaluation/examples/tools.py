from evaluation.tools.success_rate_calculator import FundamentalSuccessRateCalculator, DynamicThresholdSuccessRateCalculator
from evaluation.tools.text_editor import WordDeletion, SynonymSubstitution, ContextAwareSynonymSubstitution, DipperParaphraser, GPTParaphraser
from transformers import BertTokenizer, BertForMaskedLM, T5Tokenizer, T5ForConditionalGeneration, LlamaTokenizer, AutoModelForCausalLM, AutoTokenizer, AutoModelForSeq2SeqLM
from evaluation.tools.text_quality_analyzer import PPLCalculator, LogDiversityAnalyzer, BLEUCalculator, PassOrNotJudger, GPTTextDiscriminator
from utils.transformers_config import TransformersConfig
from watermark.auto_watermark import AutoWatermark

device = 'cuda'

def use_fundamental_success_rate_calculator():
    # Result of watermark detection
    watermarked_result = [True, True, False, True, True]
    non_watermarked_result = [False, False, False, False, False]

    # Init calculator
    calculator = FundamentalSuccessRateCalculator(labels=['TPR','F1'])

    # Calculate
    result = calculator.calculate(
                watermarked_result=watermarked_result,
                non_watermarked_result=non_watermarked_result)
    print(result)

def use_dynamic_success_rate_calculator():
    # Result of watermark detection
    watermarked_result = [5.6, 6.7, 2.6, 4.2, 10.1]
    non_watermarked_result = [1.0, -1.1, 2.4, 2.3, 1.4]

    # Init calculator
    calculator = DynamicThresholdSuccessRateCalculator(labels=['TPR','F1'],
                                                        rule='best',
                                                        target_fpr=None,
                                                        reverse=False)

    # Calculate
    result = calculator.calculate(
                watermarked_result=watermarked_result,
                non_watermarked_result=non_watermarked_result)
    print(result)

text = "The sun peeked through the clouds, casting a warm glow on the tranquil meadow. A gentle breeze rustled the leaves of the nearby trees, creating a soothing symphony of nature. In the distance, a majestic mountain range stood tall, its snow-capped peaks reaching towards the heavens. A winding river cut through the landscape, its crystal-clear waters reflecting the vibrant colors of the surrounding flora. Birds chirped merrily as they flitted from branch to branch, while butterflies danced among the wildflowers. It was a scene of pure serenity, a testament to the breathtaking beauty of the untouched wilderness."

def use_word_deletion():
    editor = WordDeletion(ratio=0.3)
    print(editor.edit(text))

def use_synonym_substitution():
    editor = SynonymSubstitution(ratio=0.3)
    print(editor.edit(text))

def use_context_aware_synonym_substitution():
    editor = ContextAwareSynonymSubstitution(
        tokenizer=BertTokenizer.from_pretrained('/data2/shared_model/bert-large-uncased/'),
        model=BertForMaskedLM.from_pretrained('/data2/shared_model/bert-large-uncased/').to(device),
        ratio=0.3)
    print(editor.edit(text))

def use_gpt_paraphraser():
    editor = GPTParaphraser(openai_model='gpt-3.5-turbo', 
                            prompt='Please rewrite the following text: ')
    print(editor.edit(text))

def use_dipper_paraphraser():
    editor = DipperParaphraser(tokenizer=T5Tokenizer.from_pretrained('/data2/shared_model/google/t5-v1_1-xxl/'),
                               model=T5ForConditionalGeneration.from_pretrained('/data2/shared_model/kalpeshk2011/dipper-paraphraser-xxl/', device_map='auto'),
                               lex_diversity=60, order_diversity=0, sent_interval=1, 
                               max_new_tokens=100, do_sample=True, top_p=0.75, top_k=None)
    print(editor.edit(text, reference=''))

def use_ppl_calculator():
    calculator = PPLCalculator(
        tokenizer=LlamaTokenizer.from_pretrained('/data2/shared_model/llama-7b/'),
        model=AutoModelForCausalLM.from_pretrained('/data2/shared_model/llama-7b/', device_map='auto'),
        device=device)
    print(calculator.analyze(text))

def use_log_diversity_analyzer():
    analyzer = LogDiversityAnalyzer()
    print(analyzer.analyze(text))

def use_bleu_calculator():
    tokenizer = AutoTokenizer.from_pretrained("/data2/shared_model/facebook/nllb-200-distilled-600M/", src_lang="deu_Latn")
    transformers_config = TransformersConfig(model=AutoModelForSeq2SeqLM.from_pretrained("/data2/shared_model/facebook/nllb-200-distilled-600M/").to(device),
                                                tokenizer=tokenizer,
                                                device=device,
                                                vocab_size=256206,
                                                forced_bos_token_id=tokenizer.lang_code_to_id["eng_Latn"])
    watermark = AutoWatermark.load('KGW',
                                   'config/KGW.json',
                                   transformers_config=transformers_config)
    
    prompt = "Die Premierminister Indiens und Japans trafen sich in Tokio."
    reference = "India and Japan prime ministers meet in Tokyo."

    watermarked_text = watermark.generate_watermarked_text(prompt)

    calculator = BLEUCalculator()
    print(calculator.analyze(text=watermarked_text, reference=reference))

def use_gpt_text_discriminator():
    tokenizer = AutoTokenizer.from_pretrained("/data2/shared_model/facebook/nllb-200-distilled-600M/", src_lang="deu_Latn")
    transformers_config = TransformersConfig(model=AutoModelForSeq2SeqLM.from_pretrained("/data2/shared_model/facebook/nllb-200-distilled-600M/").to(device),
                                                tokenizer=tokenizer,
                                                device=device,
                                                vocab_size=256206,
                                                forced_bos_token_id=tokenizer.lang_code_to_id["eng_Latn"])
    watermark = AutoWatermark.load('KGW',
                                   'config/KGW.json',
                                   transformers_config=transformers_config)
    
    prompt = "Die Premierminister Indiens und Japans trafen sich in Tokio."

    watermarked_text = watermark.generate_watermarked_text(prompt)
    unwatermarked_text = watermark.generate_watermarked_text(prompt)

    analyzer = GPTTextDiscriminator(openai_model='gpt-4', 
                                    task_description='Translate the following German text to English.')
    
    print(analyzer.analyze(text1=watermarked_text,
                           text2=unwatermarked_text,
                           question=prompt))

def use_pass_or_not_judger():
    transformers_config = TransformersConfig(model=AutoModelForCausalLM.from_pretrained("/data2/shared_model/starcoder/", device_map='auto'),
                                             tokenizer=AutoTokenizer.from_pretrained("/data2/shared_model/starcoder/"),
                                             device=device,
                                             min_length=200,
                                             max_length=400)
    watermark = AutoWatermark.load('KGW',
                                   'config/KGW.json',
                                   transformers_config=transformers_config)
    
    prompt = "\n\ndef strlen(string: str) -> int:\n    \"\"\" Return length of given string\n\"\"\""
    reference = {'task': prompt,
                 'test': "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate('') == 0\n    assert candidate('x') == 1\n    assert candidate('asdasnakj') == 9\n",
                 'entry_point': "strlen"}
    
    watermarked_text = watermark.generate_watermarked_text(prompt)

    # post-processing
    truncated_text = watermarked_text[len(prompt):]
    truncated_text = truncated_text.lstrip("\n")
    truncated_text = truncated_text.split("\n\n")[0]

    judger = PassOrNotJudger()
    print(judger.analyze(truncated_text, reference))


# use_ppl_calculator()
# use_log_diversity_analyzer()
# use_bleu_calculator()
# use_gpt_text_discriminator()
use_pass_or_not_judger()
