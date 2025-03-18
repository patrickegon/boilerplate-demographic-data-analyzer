import pandas as pd

def calculate_demographic_data():
    # Carregar os dados
    df = pd.read_csv('adult.data.csv')

    # 1. Contagem de pessoas por raça
    race_count = df['race'].value_counts()

    # 2. Média de idade dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Porcentagem de pessoas com bacharelado
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1
    )

    # 4. Porcentagem de educação avançada (>50K)
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = round(
        (higher_education['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Porcentagem de educação não avançada (>50K)
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = round(
        (lower_education['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Mínimo de horas trabalhadas por semana
    min_work_hours = df['hours-per-week'].min()

    # 7. Porcentagem que trabalha o mínimo e ganha >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 8. País com maior porcentagem de >50K
    country_salary = df.groupby('native-country')['salary'].apply(
        lambda x: round((x == '>50K').mean() * 100, 1)
    )
    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = country_salary.max()

    # 9. Ocupação mais popular na Índia (>50K)
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation'].value_counts().idxmax()
    )

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
