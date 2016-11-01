from django.db import models
from django.core.validators import MaxValueValidator


class MainSliderBlock(models.Model):
    is_active = models.BooleanField(
        verbose_name="Отображать блок",
        default=True,
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок Слайдер"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)


class SlideRecord(models.Model):
    main_block = models.ForeignKey(
        MainSliderBlock,
        verbose_name="Блок слайдера",
        related_name='records',
    )

    is_active = models.BooleanField(
        verbose_name="Активен",
        default=True,
    )

    index = models.PositiveSmallIntegerField(
        verbose_name="Номер слайда",
        blank=True,
        null=True,
        help_text="В этом порядке будут показаны слайды на первом экране"
    )

    image = models.ImageField(
        verbose_name="Изображение слайда",
        upload_to="main_slider",
        help_text="Не менее 1920px в ширину",
    )

    header = models.CharField(
        verbose_name="Заголовок",
        max_length=255
    )

    subheader = models.CharField(
        verbose_name="Подзаголовок",
        max_length=255,
    )

    first_slogan = models.CharField(
        verbose_name="Слоган",
        max_length=255,
    )

    second_slogan = models.CharField(
        verbose_name="Второй слоган",
        max_length=255,
    )

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
        ordering = ('index',)

    def __str__(self):
        return self.header


class AboutMeBlock(models.Model):
    is_active = models.BooleanField(
        verbose_name="Отображать блок",
        default=True,
    )

    full_name = models.CharField(
        verbose_name="Полное имя",
        max_length=255,
    )

    birthday = models.CharField(
        verbose_name="Дата рождения",
        max_length=20,
    )

    birthplace = models.CharField(
        verbose_name="Место рождения",
        max_length=255,
    )

    hobbies = models.CharField(
        verbose_name="Хобби",
        max_length=127,
    )

    photo = models.ImageField(
        verbose_name="Фотография",
        upload_to="about",
    )

    address = models.CharField(
        verbose_name="Адрес",
        max_length=255,
    )

    phone = models.CharField(
        verbose_name="Телефон",
        max_length=127,
    )

    email = models.CharField(
        verbose_name="Email",
        max_length=63,
    )

    skype = models.CharField(
        verbose_name="Skype",
        max_length=63,
    )

    short_info = models.CharField(
        verbose_name="Краткая информация",
        max_length=255,
    )

    long_info = models.CharField(
        verbose_name="Полная информация",
        max_length=4095
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок Обо мне"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)


class AwardsBlock(models.Model):
    is_active = models.BooleanField(
        verbose_name="Отображать блок",
        default=True,
    )

    description = models.CharField(
        verbose_name="Описание, блок Достижения",
        max_length=4095,
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок Достижения"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)


class AwardRecord(models.Model):
    award_block = models.ForeignKey(
        AwardsBlock,
        verbose_name="Блок достижений",
        related_name="records",
    )

    is_active = models.BooleanField(
        verbose_name="Активна",
        default=True,
    )

    index = models.PositiveSmallIntegerField(
        verbose_name="Порядковый номер",
        blank=True,
        null=True,
    )

    title = models.CharField(
        verbose_name="Название достижения",
        max_length=255,
    )

    company_name = models.CharField(
        verbose_name="Название компании",
        max_length=255,
    )

    date = models.CharField(
        verbose_name="Дата вручения",
        max_length=63,
    )

    image = models.ImageField(
        verbose_name="Изображение достижения",
        upload_to="award",
    )

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"
        ordering = ('index',)

    def __str__(self):
        return self.title


class VideoBlock(models.Model):
    is_active = models.BooleanField(
        verbose_name="Отображать блок",
        default=False,
    )

    video = models.FileField(
        verbose_name="Файл видео",
        upload_to="video",
        blank=True,
        null=True,
    )

    video_link = models.CharField(
        verbose_name="Ссылка на видео",
        max_length=255,
        blank=True,
        null=True,
    )

    video_title = models.CharField(
        verbose_name="Текст над видео",
        max_length=1023,
    )

    video_footer = models.CharField(
        verbose_name="Текст под видео",
        max_length=1023,
    )

    background_image = models.ImageField(
        verbose_name="Фоновое изображение для блока видео",
        upload_to="video",
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок Видео"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)


class EducationBlock(models.Model):
    is_active = models.BooleanField(
        verbose_name="Отображать блок",
        default=True,
    )

    description = models.CharField(
        verbose_name="Описание, блок Образование",
        max_length=4095,
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок Образование"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)


class EducationRecord(models.Model):
    education_block = models.ForeignKey(
        EducationBlock,
        verbose_name="Блок образования",
        related_name="records",
    )

    is_active = models.BooleanField(
        verbose_name="Активна",
        default=True,
    )

    index = models.PositiveSmallIntegerField(
        verbose_name="Порядковый номер",
        blank=True,
        null=True,
    )

    grade = models.CharField(
        verbose_name="Степень, звание",
        max_length=127,
    )

    university_name = models.CharField(
        verbose_name="Название учебного заведения",
        max_length=255,
    )

    country = models.CharField(
        verbose_name="Страна",
        max_length=127,
    )

    date_period = models.CharField(
        verbose_name="Период обучения",
        max_length=255,
    )

    description = models.CharField(
        verbose_name="Описание",
        max_length=511,
    )

    class Meta:
        verbose_name = "Запись об образовании"
        verbose_name_plural = "Записи об образовании"
        ordering = ('index',)

    def __str__(self):
        return "{0} {1}".format(self.grade, self.date_period)


class PortfolioBlock(models.Model):
    is_active = models.BooleanField(
        verbose_name="Отображать блок",
        default=True,
    )

    description = models.CharField(
        verbose_name="Описание, блок Портфолио",
        max_length=4095,
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок Портфолио"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)


class PortfolioType(models.Model):
    is_active = models.BooleanField(
        verbose_name="Активен",
        default=True,
    )

    name = models.CharField(
        verbose_name="Название",
        max_length=31,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип работы в портфолио"
        verbose_name_plural = "Типы работы в портфолио"


class PortfolioRecord(models.Model):
    portfolio_block = models.ForeignKey(
        PortfolioBlock,
        verbose_name="Блок портфолио",
        related_name="records",
    )

    is_active = models.BooleanField(
        verbose_name="Активна",
        default=True,
    )

    index = models.PositiveSmallIntegerField(
        verbose_name="Порядковый номер",
        blank=True,
        null=True,
    )

    header = models.CharField(
        verbose_name="Заголовок",
        max_length=127,
    )

    subHeader = models.CharField(
        verbose_name="Подзаголовок",
        max_length=255,
        blank=True,
        null=True,
    )

    image = models.ImageField(
        verbose_name="Изображение работы",
        upload_to="portfolio",
    )

    url = models.URLField(
        verbose_name="Ссылка на работу",
        blank=True,
        null=True,
    )

    portfolio_type = models.ManyToManyField(
        PortfolioType,
        verbose_name="Типы работ",
        related_name="portfolio_types"
    )

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "Запись в портфолио"
        verbose_name_plural = "Записи в портфолио"
        ordering = ('index',)


class ProcessBlock(models.Model):
    is_active = models.BooleanField(
        verbose_name="Отображать блок",
        default=True,
    )

    description = models.CharField(
        verbose_name="Описание, блок Процессы",
        max_length=4095,
    )

    background = models.ImageField(
        verbose_name="Фоновое изображение",
        upload_to="process",
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок Процессы"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)


class ProcessRecord(models.Model):
    process_block = models.ForeignKey(
        ProcessBlock,
        verbose_name="Блок процессов",
        related_name="records",
    )

    is_active = models.BooleanField(
        verbose_name="Активна",
        default=True,
    )

    index = models.PositiveSmallIntegerField(
        verbose_name="Порядковый номер",
        blank=True,
        null=True,
    )

    name = models.CharField(
        verbose_name="Название процесса",
        max_length=63,
    )

    icon = models.CharField(
        verbose_name="Класс иконки",
        max_length=31,
        help_text="(FontAwesome)",
    )

    class Meta:
        verbose_name = "Запись о процессе"
        verbose_name_plural = "Записи о процессах"
        ordering = ('index',)

    def __str__(self):
        return self.name


class ServiceBlock(models.Model):
    is_active = models.BooleanField(
        verbose_name="Отображать блок",
        default=True,
    )

    description = models.CharField(
        verbose_name="Описание блока",
        max_length=4095,
    )

    background = models.ImageField(
        verbose_name="Фоновое изображение",
        upload_to="service",
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок Услуги"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)


class ServiceRecord(models.Model):
    service_block = models.ForeignKey(
        ServiceBlock,
        verbose_name="Блок услуг",
        related_name="records",
    )

    index = models.PositiveSmallIntegerField(
        verbose_name="Порядковый номер",
        blank=True,
        null=True,
    )

    name = models.CharField(
        verbose_name="Название услуги",
        max_length=255,
    )

    description = models.CharField(
        verbose_name="Описание услуги",
        max_length=1023,
    )

    icon = models.CharField(
        verbose_name="Класс иконки",
        max_length=31,
        help_text="(FontAwesome)",
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ('index',)

    def __str__(self):
        return self.name


class SkillBlock(models.Model):
    is_active = models.BooleanField(
        verbose_name="Отображать блок",
        default=True,
    )

    description = models.CharField(
        verbose_name="Описание блока",
        max_length=4095,
    )

    background = models.ImageField(
        verbose_name="Фоновое изображение",
        upload_to="service",
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок Навыки"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)


class SkillRecord(models.Model):
    skill_block = models.ForeignKey(
        SkillBlock,
        verbose_name="Блок навыков",
        related_name="records",
    )

    is_active = models.BooleanField(
        verbose_name="Активен",
        default=True,
    )

    index = models.PositiveSmallIntegerField(
        verbose_name="Порядковый номер",
        blank=True,
        null=True,
    )

    title = models.CharField(
        verbose_name="Название",
        max_length=127,
    )

    persent = models.PositiveSmallIntegerField(
        verbose_name="Процентное соотношение",
        validators=[
            MaxValueValidator(100),
        ],
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Запись о навыке"
        verbose_name_plural = "Записи о навыках"
        ordering = ('index',)

    def __str__(self):
        return self.title


class TestimonialsBlock(models.Model):
    is_active = models.BooleanField(
        verbose_name="Отображать блок",
        default=True,
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок Рекомендации"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)


class TestimonialRecord(models.Model):
    testimonial_block = models.ForeignKey(
        TestimonialsBlock,
        verbose_name="Блок рекомендаций",
        related_name="records",
    )

    is_active = models.BooleanField(
        verbose_name="Активен",
        default=True,
    )

    index = models.PositiveSmallIntegerField(
        verbose_name="Порядковый номер",
        blank=True,
        null=True,
    )

    name = models.CharField(
        verbose_name="Имя рекомендателя",
        max_length=127,
    )

    companyName = models.CharField(
        verbose_name="Название компании",
        max_length=127,
    )

    text = models.CharField(
        verbose_name="Текст рекомендации",
        max_length=1023,
    )

    class Meta:
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекомендации"
        ordering = ('index',)

    def __str__(self):
        return self.name


class WorkExperienceBlock(models.Model):
    is_active = models.BooleanField(
        verbose_name="Отображать блок",
        default=True,
    )

    description = models.CharField(
        verbose_name="Описание блока",
        max_length=4095,
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок Опыт работы"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)


class WorkExperienceRecord(models.Model):
    work_experience_block = models.ForeignKey(
        WorkExperienceBlock,
        verbose_name="Блок опыта работы",
        related_name="records",
    )

    is_active = models.BooleanField(
        verbose_name="Активен",
        default=True,
    )

    index = models.PositiveSmallIntegerField(
        verbose_name="Порядковый номер",
        blank=True,
        null=True,
    )

    companyName = models.CharField(
        verbose_name="Название компании",
        max_length=127,
    )

    position = models.CharField(
        verbose_name="Должность",
        max_length=127,
    )

    date_period = models.CharField(
        verbose_name="Период работы",
        max_length=127,
    )

    description = models.CharField(
        verbose_name="Описание",
        max_length=255,
        blank=True,
        null=True,
    )

    companyUrl = models.URLField(
        verbose_name="Ссылка на сайт компании",
        max_length=255,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Запись об опыте работы"
        verbose_name_plural = "Записи об опыте работы"
        ordering = ('index',)

    def __str__(self):
        return "{0} {1}".format(self.companyName, self.date_period)


class CVBlock(models.Model):
    is_active = models.BooleanField(
        verbose_name="Отображать блок",
        default=True,
    )

    cv = models.FileField(
        verbose_name="Файл Резюме",
        upload_to="cv",
        help_text="рекомендуется формат PDF"
    )

    description = models.CharField(
        verbose_name="Описание для ссылки с резюме",
        max_length=4095,
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок Резюме"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)


class GetInTouchBlock(models.Model):
    is_active = models.BooleanField(
        verbose_name="Отображать блок",
        default=True,
    )

    description = models.CharField(
        verbose_name="Описание",
        max_length=4095,
    )

    description_social = models.CharField(
        verbose_name="Описание (соц. сети)",
        max_length=4095,
    )

    SOCIAL_NETWORKS = (
        ("vk", "Вконтакте"),
        ("fb", "Facebook"),
        ("li", "Linked.In"),
        ("gp", "Google Plus"),
        ("ig", "Instagram"),
        ("bh", "Behance"),
        ("fl", "Freelance"),
    )

    SOCIAL_NETWORK_ICONS = (
        ("vk", "fa-vk"),
        ("fb", "fa-facebook"),
        ("li", "fa-linkedin"),
        ("gp", "fa-googleplus"),
        ("ig", "fa-instagram"),
        ("bh", "fa-behance"),
        ("fl", "fa-freelance"),
    )

    signature = models.ImageField(
        verbose_name="Изображение подписи",
        upload_to="common",
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок Обратная связь"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)


class SocialRecord(models.Model):
    getintouch_block = models.ForeignKey(
        GetInTouchBlock,
        verbose_name="Блок обратной связи",
        related_name="records",
    )

    is_active = models.BooleanField(
        verbose_name="Активна",
        default=True,
    )

    index = models.PositiveSmallIntegerField(
        verbose_name="Порядковый номер",
        blank=True,
        null=True,
    )

    link = models.URLField(
        verbose_name="Ссылка",
        max_length=255,
    )

    type = models.CharField(
        verbose_name="Тип соц.сети",
        choices=GetInTouchBlock.SOCIAL_NETWORKS,
        max_length=10,
    )

    class Meta:
        verbose_name = "Запись о соц.сети"
        verbose_name_plural = "Записи о соц.сетях"
        ordering = ('index',)

    def __str__(self):
        return self.link


class Settings(models.Model):
    show_section_buttons = models.BooleanField(
        verbose_name="Показывать кнопки секций",
        default=True,
    )

    show_animation = models.BooleanField(
        verbose_name="Использовать анимацию",
        default=True,
    )

    feedback_mail = models.EmailField(
        verbose_name="Основной Email",
        max_length=127,
        help_text="Почта, куда отправлять сообщения из формы обратной связи",
    )

    class Meta:
        verbose_name = verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "{0} #{1}".format(self._meta.verbose_name, self.id)
