from quiz import Question, VoteEnum

questions_database = [
    Question("?האם לדעתך צריך להגדיל את תקציב הביטחון, גם אם הדבר בא על חשבון תקציבים אזרחיים",
             {
                 "יהדות התורה": VoteEnum.AGREE,
                 "הליכוד": VoteEnum.AGREE,
                 "מרצ": VoteEnum.DISAGREE,
                 "ישראל ביתנו": VoteEnum.DISAGREE,
                 "הבית היהודי": VoteEnum.DISAGREE,
                 "הרשימה המשותפת": VoteEnum.DISAGREE,
                 "יש עתיד": VoteEnum.DISAGREE,
                 "שס": VoteEnum.PASSIVE,
                 "כחול לבן": VoteEnum.PASSIVE,  # ###################
                 "העבודה": VoteEnum.PASSIVE,  # #######################
             }
    ),

    Question("?האם את/ה בעד תחבורה ציבורית בשבת",
             {
                 "יהדות התורה": VoteEnum.DISAGREE,
                 "הליכוד": VoteEnum.DISAGREE,
                 "מרצ": VoteEnum.AGREE,
                 "ישראל ביתנו": VoteEnum.AGREE,
                 "הבית היהודי": VoteEnum.DISAGREE,
                 "הרשימה המשותפת": VoteEnum.AGREE,
                 "יש עתיד": VoteEnum.AGREE,
                 "שס": VoteEnum.DISAGREE,
                 "כחול לבן": VoteEnum.AGREE,
                 "העבודה": VoteEnum.AGREE,
             }
    ),

    Question("""?האם לדעתך צריך להוריד את המע"מ עעל מוצרי מזון בסיסיים""",
             {
                 "יהדות התורה": VoteEnum.AGREE,
                 "הליכוד": VoteEnum.AGREE,
                 "מרצ": VoteEnum.AGREE,
                 "ישראל ביתנו": VoteEnum.DISAGREE,
                 "הבית היהודי": VoteEnum.DISAGREE,
                 "הרשימה המשותפת": VoteEnum.AGREE,
                 "יש עתיד": VoteEnum.DISAGREE,
                 "שס": VoteEnum.AGREE,
                 "כחול לבן": VoteEnum.AGREE, # ################
                 "העבודה": VoteEnum.AGREE, # #######################
             }
    ),

    Question("?האם אתה בעד לתת עונש מוות למחבלים",
             {
                 "יהדות התורה": VoteEnum.DISAGREE,
                 "הליכוד": VoteEnum.PASSIVE,
                 "מרצ": VoteEnum.DISAGREE,
                 "ישראל ביתנו": VoteEnum.AGREE,
                 "הבית היהודי": VoteEnum.PASSIVE,
                 "הרשימה המשותפת": VoteEnum.DISAGREE,
                 "יש עתיד": VoteEnum.DISAGREE,
                 "שס": VoteEnum.DISAGREE,
                 "כחול לבן": VoteEnum.DISAGREE,
                 "העבודה": VoteEnum.DISAGREE,
             }
    ),

    Question("""?האם לדעתך צריך לאשר נישואים להט"בים""",
             {
                 "יהדות התורה": VoteEnum.DISAGREE,
                 "הליכוד": VoteEnum.AGREE,
                 "מרצ": VoteEnum.AGREE,
                 "ישראל ביתנו": VoteEnum.DISAGREE,
                 "הבית היהודי": VoteEnum.DISAGREE,
                 "הרשימה המשותפת": VoteEnum.AGREE,
                 "יש עתיד": VoteEnum.AGREE,
                 "שס": VoteEnum.DISAGREE,
                 "כחול לבן": VoteEnum.AGREE,
                 "העבודה": VoteEnum.AGREE,
             }
    ),

    Question("?האם צריכה להיות לגליזציה לסמים קלים בישראל",
             {
                 "יהדות התורה": VoteEnum.DISAGREE,
                 "הליכוד": VoteEnum.PASSIVE,
                 "מרצ": VoteEnum.AGREE,
                 "ישראל ביתנו": VoteEnum.PASSIVE,
                 "הבית היהודי": VoteEnum.PASSIVE,
                 "הרשימה המשותפת": VoteEnum.DISAGREE,
                 "יש עתיד": VoteEnum.PASSIVE,
                 "שס": VoteEnum.PASSIVE,
                 "כחול לבן": VoteEnum.PASSIVE,
                 "העבודה": VoteEnum.AGREE,
             }
    ),

    Question("?האם אתה בעד גיוס בני ישיבות",
             {
                 "יהדות התורה": VoteEnum.DISAGREE,
                 "הליכוד": VoteEnum.PASSIVE,
                 "מרצ": VoteEnum.DISAGREE,
                 "ישראל ביתנו": VoteEnum.AGREE,
                 "הבית היהודי": VoteEnum.PASSIVE,
                 "הרשימה המשותפת": VoteEnum.DISAGREE,
                 "יש עתיד": VoteEnum.DISAGREE,
                 "שס": VoteEnum.DISAGREE,
                 "כחול לבן": VoteEnum.AGREE,
                 "העבודה": VoteEnum.AGREE,
             }
    ),
     Question("?האם לדעתך צריך לחוקק חוק שיגביל את שכר המנהלים הבכירים בחברות ציבוריות בכל המשק",
             {
                 "יהדות התורה": VoteEnum.AGREE,
                 "הליכוד": VoteEnum.DISAGREE,
                 "מרצ": VoteEnum.AGREE,
                 "ישראל ביתנו": VoteEnum.DISAGREE,
                 "הבית היהודי": VoteEnum.DISAGREE,
                 "הרשימה המשותפת": VoteEnum.AGREE,
                 "יש עתיד": VoteEnum.AGREE,
                 "שס": VoteEnum.PASSIVE,
                 "כחול לבן": VoteEnum.PASSIVE,  # ##################
                 "העבודה": VoteEnum.PASSIVE,  # ########################
             }
    ),
    Question("?האם לדעתך המדינה צריכה להטיל מסים גבוהים יותר ולתת בתמורה שירותים ציבוריים נרחבים יותר",
             {
                 "יהדות התורה": VoteEnum.AGREE,
                 "הליכוד": VoteEnum.DISAGREE,
                 "מרצ": VoteEnum.AGREE,
                 "ישראל ביתנו": VoteEnum.DISAGREE,
                 "הבית היהודי": VoteEnum.DISAGREE,
                 "הרשימה המשותפת": VoteEnum.DISAGREE,
                 "יש עתיד": VoteEnum.DISAGREE,
                 "שס": VoteEnum.PASSIVE,
                 "כחול לבן": VoteEnum.PASSIVE,  # ###########
                 "העבודה": VoteEnum.PASSIVE,  # ################
             }
    ),
    Question("?האם לדעתך בגלל העלייה בתוחלת החיים, צריך להעלות את גיל הפרישה",
             {
                 "יהדות התורה": VoteEnum.AGREE,
                 "הליכוד": VoteEnum.AGREE,
                 "מרצ": VoteEnum.DISAGREE,
                 "ישראל ביתנו": VoteEnum.DISAGREE,
                 "הבית היהודי": VoteEnum.AGREE,
                 "הרשימה המשותפת": VoteEnum.DISAGREE,
                 "יש עתיד": VoteEnum.DISAGREE,
                 "שס": VoteEnum.PASSIVE,
                 "כחול לבן": VoteEnum.PASSIVE,  # ###########
                 "העבודה": VoteEnum.PASSIVE,  # ################
             }
    ),
    Question("?האם לדעתך המדינה צריכה להשקיע מיליארדים בבניית דיור ציבורי לאנשים מתחת לקו העוני",
             {
                 "יהדות התורה": VoteEnum.PASSIVE,
                 "הליכוד": VoteEnum.DISAGREE,
                 "מרצ": VoteEnum.AGREE,
                 "ישראל ביתנו": VoteEnum.AGREE,
                 "הבית היהודי": VoteEnum.DISAGREE,
                 "הרשימה המשותפת": VoteEnum.AGREE,
                 "יש עתיד": VoteEnum.DISAGREE,
                 "שס": VoteEnum.PASSIVE,
                 "כחול לבן": VoteEnum.PASSIVE,  # ###########
                 "העבודה": VoteEnum.PASSIVE,  # ################
             }
    ),
    Question("?האם לדעתך כספי המיסים צריכים להיות חלק גדול יותר מהפנסיה של העובדים המבוגרים",
             {
                 "יהדות התורה": VoteEnum.PASSIVE,
                 "הליכוד": VoteEnum.DISAGREE,
                 "מרצ": VoteEnum.AGREE,
                 "ישראל ביתנו": VoteEnum.AGREE,
                 "הבית היהודי": VoteEnum.DISAGREE,
                 "הרשימה המשותפת": VoteEnum.PASSIVE,
                 "יש עתיד": VoteEnum.DISAGREE,
                 "שס": VoteEnum.PASSIVE,
                 "כחול לבן": VoteEnum.PASSIVE,  # ###########
                 "העבודה": VoteEnum.PASSIVE,  # ################
             }
    ),
    Question("?האם לדעתך הכנסת ניתוחים פרטיים בתשלום לבתי החולים הציבוריים תציל את מערכת הבריאות",
             {
                 "יהדות התורה": VoteEnum.AGREE,
                 "הליכוד": VoteEnum.AGREE,
                 "מרצ": VoteEnum.DISAGREE,
                 "ישראל ביתנו": VoteEnum.AGREE,
                 "הבית היהודי": VoteEnum.AGREE,
                 "הרשימה המשותפת": VoteEnum.DISAGREE,
                 "יש עתיד": VoteEnum.DISAGREE,
                 "שס": VoteEnum.PASSIVE,
                 "כחול לבן": VoteEnum.PASSIVE,  # ###########
                 "העבודה": VoteEnum.PASSIVE,  # ################
             }
    ),
    Question("?האם לדעתך המדינה יכולה ליצור תחרות בשוק הגז הטבעי על ידי פירוק המונופול, גם בלי צורך לפקח על מחירי הגז",
             {
                 "יהדות התורה": VoteEnum.PASSIVE,
                 "הליכוד": VoteEnum.AGREE,
                 "מרצ": VoteEnum.DISAGREE,
                 "ישראל ביתנו": VoteEnum.AGREE,
                 "הבית היהודי": VoteEnum.AGREE,
                 "הרשימה המשותפת": VoteEnum.PASSIVE,
                 "יש עתיד": VoteEnum.DISAGREE,
                 "שס": VoteEnum.PASSIVE,
                 "כחול לבן": VoteEnum.PASSIVE,  # ###########
                 "העבודה": VoteEnum.PASSIVE,  # ################
             }
    )
]






