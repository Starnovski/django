from django.test import TestCase
from .models import Post, Category
import random
# Create your tests here.

number = 1
categories = Category.objects.all()

titles = ["The standard Lorem Ipsum passage, used since the 1500s",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "Section 1.10.32 of de Finibus Bonorum et Malorum, written by Cicero in 45 BC",
            "1914 translation by H. Rackham"]


while number < 40:
    cat = random.choice(categories)
    text = random.choice(titles)
    post = Post(title = text, body = """Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium
            totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo
            enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione
            voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed
            quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam,
            quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum
            iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?""",
            category = cat)

    post.save()
    number += 1
    print('.')
