import praw
import argparse
import logging

LOG_LEVEL = logging.INFO
LOG_FORMAT = '[%(levelname)8s] %(asctime)s %(filename)20s@%(lineno)4s %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT, level=LOG_LEVEL)


def main():
    args = parse_arguments()

    reddit = praw.Reddit('bot')
    subreddit = reddit.subreddit(args.subreddit)

    for submission in subreddit.stream.submissions():
        question = filter_titles_naively_qm(submission.title)
        if question:
            logging.info('Q: %s', question)
            logging.info('A: %s', answer(question))


def parse_arguments():
    parser = argparse.ArgumentParser(description='Open AI GPT-2 autoreply to reddit')
    parser.add_argument('-r', '--subreddit', default='ITdept', required=False)
    parser.add_argument('-m', '--model', default='117M', required=False)
    return parser.parse_args()

def filter_titles_naively(title):
    ret = ''
    questions = ['what is', 'who is', 'what are', 'where to', 'how to']
    questions = ['?']
    # Ignore titles with more than 10 words as they probably are not simple questions.
    normalized_title = title.lower()
    for question_phrase in questions:
        if question_phrase in normalized_title:
            ret = title
            break
    return ret

def filter_titles_naively_qm(title):
    ret = ''
    normalized_title = title.lower()
    if '?' in normalized_title:
            ret = title
    return ret

def answer(question):
    return 'oh man!'

def configure_gpt2():
    models_dir = ''

if __name__ == '__main__':
    main()

