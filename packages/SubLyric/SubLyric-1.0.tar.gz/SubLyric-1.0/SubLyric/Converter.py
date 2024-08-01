import re
'''
This library is used to convert srt files to lrc files and vice versa.
'''
def round_ms(ms):
    '''
    This function is used to round milliseconds to give slightly more accurate timings.
    Example: ms = '256' First, int(ms) to make it an integerate to use round(). We'll divide it by 1000 to make it in decimals.
    temp_ms = 0.256 and then you round it by 2 Decimals. temp_ms = 0.26
    new_ms returns temp_ms into a string and gets the numbers needed only.
    new_ms = '26'
    '''
    temp_ms = round(int(ms)/1000, 2)
    new_ms = str(temp_ms)[2:]
    return new_ms

def srt_to_lrc(srt_file, lrc_file):
    '''
    This function converts srt files to lrc.
    '''
    if srt_file.endswith('.srt'):
        srt_file = srt_file[:-4]
    if lrc_file.endswith('.lrc'):
        lrc_file = lrc_file[:-4]
    try:
        with open(f'{srt_file}.srt', 'r', encoding='utf-8') as srt_f:
            srt_lines = srt_f.read()
            # Example:
            # 1
            # 00:00:01,918 --> 00:00:03,378
            # Hello, How are you?
    except Exception as e:
        print(f'An error occurred while reading the SRT file: {e}')
        return False
    srt_pattern = r'\d+\n\d{2}:(\d{2}):(\d{2}),(\d{3})' \
                  r'\s-->\s' \
                  r'\d{2}:\d{2}:\d{2},\d{3}\n' \
                  r'(.*)\n?'
    lrc_lines = re.findall(srt_pattern, srt_lines)
    # ['('00', '01', '918', 'Hello, How are you?')', '(minutes, seconds, ms, lyrics)', etc...]
    # '(minutes, seconds, ms, lyrics)'
    if len(lrc_lines) == 0:
        print('Error: SRT file is empty.')
        return False
    final_text = ''
    for i in range(len(lrc_lines)):
        minutes, seconds, ms, lyrics = lrc_lines[i]
        ms = round_ms(ms)
        final_text += f'[{minutes}:{seconds}.{ms}]{lyrics}' # lrc files format.
        # [00:01.91]Hello, How are you?
        if i != len(lrc_lines)-1:
            final_text += '\n'  # Just for accuarcy. To not have an empty line at the end of the file.

    with open (f'{lrc_file}.lrc', 'w', encoding='utf-8') as lrc_f:
        lrc_f.write(final_text)
        print('SRT to LRC conversion successful')
        return True

def lrc_to_srt(lrc_file, srt_file):
    '''
    This function converts lrc files to srt.
    '''
    if srt_file.endswith('.srt'):
        srt_file = srt_file[:-4]
    if lrc_file.endswith('.lrc'):
        lrc_file = lrc_file[:-4]
    try:
        with open(f'{lrc_file}.lrc', 'r', encoding='utf-8') as lrc_f:
            lrc_lines = lrc_f.read()
    except Exception as e:
        print(f'An error occurred while reading the LRC file: {e}')
        return False
    lrc_pattern = r'\[(\d{2}):(\d{2})\.(\d{2})\](.*)'
    # Pattern: [00:01.91]Hello, How are you?
    srt_lines = re.findall(lrc_pattern, lrc_lines)
    if len(srt_lines) == 0:
        print('Error: LRC file is empty.')
        return False
    final_text = ''
    for i in range(len(srt_lines)):
        # srt files use 2 times for each subtitle. 'starting_time --> ending_time'
        # Noting that ending_time equals starting_time for the next line, you can get its value by using i+1.
        minutes, seconds, ms, lyrics = srt_lines[i]
        minutes2, seconds2, ms2, lyrics2 = srt_lines[i+1] if (i != len(srt_lines)-1) else (str(int(minutes)+1), seconds, ms, '')
        # lrc files don't have ending_time like srt files. Threfore, a custom value must be set.
        # 1 minute extra is reasonable since lrc files are used for songs so it should be fine.
        final_text += f'{i+1}\n00:{minutes}:{seconds},{ms}0 --> 00:{minutes2}:{seconds2},{ms2}0\n{lyrics}'
        if i != len(srt_lines)-1:
            final_text += '\n\n'
            # Adding 2 new lines to fit the format of srt files except for the final line.
            # Can be added in the original final_text += line but i separated it juts for accuarcy.
            # To not have 2 empty lines at the end of the file.
    with open(f'{srt_file}.srt', 'w', encoding='utf-8') as srt_f:
        srt_f.write(final_text)
        print('LRC to SRT conversion successful')
        return True
