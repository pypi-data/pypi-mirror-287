from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, Field, PrivateAttr

if TYPE_CHECKING:
    from nubela_api.models.response import Response

class PersonView(BaseModel):
    link: Optional[str] = Field(None, description="Link to the person's profile.")
    name: Optional[str] = Field(None, description="Name of the person.")
    summary: Optional[str] = Field(None, description="Summary of the person.")
    location: Optional[str] = Field(None, description="Location of the person.")

class Date(BaseModel):
    day: Optional[int] = Field(None, description="Day of the date.")
    month: Optional[int] = Field(None, description="Month of the date.")
    year: Optional[int] = Field(None, description="Year of the date.")

class TestScore(BaseModel):
    name: Optional[str] = Field(None, description="Name of the test.")
    score: Optional[str] = Field(None, description="Score achieved.")
    date_on: Optional[Date] = Field(None, description="Date the test was taken.")
    description: Optional[str] = Field(None, description="Description of the test.")

class Patent(BaseModel):
    title: Optional[str] = Field(None, description="Title of the patent.")
    issuer : Optional[str] = Field(None, description="Issuer of the patent.")
    issued_on: Optional[Date] = Field(None, description="Date the patent was issued.")
    description: Optional[str] = Field(None, description="Description of the patent.")
    url: Optional[str] = Field(None, description="URL of the patent.")
    application_number: Optional[str] = Field(None, description="Application number of the patent.")
    patent_number: Optional[str] = Field(None, description="Patent number.")
    
class Group(BaseModel):
    name: Optional[str] = Field(None, description="Name of the group.")
    url: Optional[str] = Field(None, description="URL of the group.")
    profile_pic_url: Optional[str] = Field(None, description="URL of the group's profile picture.")

class Project(BaseModel):
    description: Optional[str] = Field(None, description="Project description")
    ends_at: Optional[Date] = Field(None, description="End date of the project")
    starts_at: Optional[Date] = Field(None, description="Start date of the project")
    title: Optional[str] = Field(None, description="Project title")
    url: Optional[str] = Field(None, description="URL of the project's homepage")


class Experience(BaseModel):
    starts_at: Optional[Date] = Field(None, description="Start date of the experience.")
    ends_at: Optional[Date] = Field(None, description="End date of the experience.")
    company: Optional[str] = Field(None, description="Name of the company.")
    company_linkedin_profile_url: Optional[str] = Field(
        None, description="LinkedIn profile URL of the company."
    )
    company_facebook_profile_url: Optional[str] = Field(
        None, description="Facebook profile URL of the company."
    )
    title: Optional[str] = Field(None, description="Job title.")
    description: Optional[str] = Field(None, description="Description of the experience.")
    location: Optional[str] = Field(None, description="Location of the experience.")
    logo_url: Optional[str] = Field(None, description="URL of the company's logo.")


class Education(BaseModel):
    starts_at: Optional[Date] = Field(None, description="Start date of the education.")
    ends_at: Optional[Date] = Field(None, description="End date of the education.")
    field_of_study: Optional[str] = Field(None, description="Field of study.")
    degree_name: Optional[str] = Field(None, description="Name of the degree.")
    school: Optional[str] = Field(None, description="Name of the school.")
    school_linkedin_profile_url: Optional[str] = Field(
        None, description="LinkedIn profile URL of the school."
    )
    school_facebook_profile_url: Optional[str] = Field(
        None, description="Facebook profile URL of the school."
    )
    description: Optional[str] = Field(None, description="Description of the education.")
    logo_url: Optional[str] = Field(None, description="URL of the school's logo.")
    grade: Optional[str] = Field(None, description="Grade achieved.")
    activities_and_societies: Optional[str] = Field(
        None, description="Activities and societies involved in."
    )


class AccomplishmentAward(BaseModel):
    title: Optional[str] = Field(None, description="Title of the award.")
    issuer: Optional[str] = Field(None, description="Issuer of the award.")
    issued_on: Optional[Date] = Field(None, description="Date the award was issued.")
    description: Optional[str] = Field(None, description="Description of the award.")


class AccomplishmentCourse(BaseModel):
    name: Optional[str] = Field(None, description="Name of the course.")
    number: Optional[str] = Field(None, description="Course number.")

class Organization(BaseModel):
    org_name: Optional[str] = Field(None, description="Name of the organization.")
    title: Optional[str] = Field(None, description="Title of the organization.")
    description: Optional[str] = Field(None, description="Description of the organization.")
    starts_at: Optional[Date] = Field(None, description="Start date of the organization.")
    ends_at: Optional[Date] = Field(None, description="End date of the organization.")

class Publication(BaseModel):
    name: Optional[str] = Field(None, description="Name of the publication.")
    publisher: Optional[str] = Field(None, description="Publisher of the publication.")
    published_on: Optional[Date | str] = Field(None, description="Date the publication was published.")
    description: Optional[str] = Field(None, description="Description of the publication.")
    url: Optional[str] = Field(None, description="URL of the publication.")

class VolunteerWork(BaseModel):
    starts_at: Optional[Date] = Field(None, description="Start date of the volunteer work.")
    ends_at: Optional[Date] = Field(None, description="End date of the volunteer work.")
    title: Optional[str] = Field(None, description="Title of the volunteer position.")
    cause: Optional[str] = Field(None, description="Cause associated with the volunteer work.")
    company: Optional[str] = Field(None, description="Name of the organization.")
    company_linkedin_profile_url: Optional[str] = Field(
        None, description="LinkedIn profile URL of the organization."
    )
    description: Optional[str] = Field(None, description="Description of the volunteer work.")
    logo_url: Optional[str] = Field(None, description="URL of the organization's logo.")


class Certification(BaseModel):
    starts_at: Optional[Date] = Field(None, description="Start date of certification.")
    ends_at: Optional[Date] = Field(None, description="End date of certification.")
    name: Optional[str] = Field(None, description="Name of the certification.")
    license_number: Optional[str] = Field(None, description="License number.")
    display_source: Optional[str] = Field(
        None, description="Source where certification is displayed."
    )
    authority: Optional[str] = Field(None, description="Authority that issued the certification.")
    url: Optional[str] = Field(None, description="URL related to the certification.")


class Recommendation(BaseModel):
    name: Optional[str] = Field(
        None, description="Name of the person providing the recommendation."
    )
    text: Optional[str] = Field(None, description="Text of the recommendation.")


class Activity(BaseModel):
    title: Optional[str] = Field(None, description="Title of the activity.")
    link: Optional[str] = Field(None, description="Link related to the activity.")
    activity_status: Optional[str] = Field(None, description="Status of the activity.")


class Article(BaseModel):
    title: Optional[str] = Field(None, description="Title of the article.")
    link: Optional[str] = Field(None, description="Link to the article.")
    published_date: Optional[Date] = Field(None, description="Date the article was published.")
    author: Optional[str] = Field(None, description="Author of the article.")
    image_url: Optional[str] = Field(None, description="URL of the article's image.")


class Skill(BaseModel):
    name: Optional[str] = Field(None, description="Name of the skill.")


class InferredSalary(BaseModel):
    min: Optional[float] = Field(None, description="Minimum inferred salary.")
    max: Optional[float] = Field(None, description="Maximum inferred salary.")


class Profile(BaseModel):
    public_identifier: Optional[str] = Field(None, description="Public identifier of the profile.")
    profile_pic_url: Optional[str] = Field(None, description="URL of the profile picture.")
    background_cover_image_url: Optional[str] = Field(
        None, description="URL of the background cover image."
    )
    first_name: Optional[str] = Field(None, description="First name of the profile owner.")
    last_name: Optional[str] = Field(None, description="Last name of the profile owner.")
    full_name: Optional[str] = Field(None, description="Full name of the profile owner.")
    follower_count: Optional[int] = Field(None, description="Number of followers.")
    occupation: Optional[str] = Field(None, description="Occupation of the profile owner.")
    headline: Optional[str] = Field(None, description="Headline or summary of the profile.")
    summary: Optional[str] = Field(None, description="Detailed summary of the profile.")
    country: Optional[str] = Field(None, description="Country of residence.")
    country_full_name: Optional[str] = Field(
        None, description="Full name of the country of residence."
    )
    city: Optional[str] = Field(None, description="City of residence.")
    state: Optional[str] = Field(None, description="State or region of residence.")
    experiences: Optional[list[Experience]] = Field(None, description="list of experiences.")
    education: Optional[list[Education]] = Field(None, description="list of educations.")
    languages: Optional[list[str]] = Field(None, description="list of languages known.")
    accomplishment_organisations: Optional[list[Organization | str]] = Field(
        None, description="list of organizational accomplishments."
    )
    accomplishment_publications: Optional[list[Publication | str]] = Field(
        None, description="list of publications."
    )
    accomplishment_honors_awards: Optional[list[AccomplishmentAward]] = Field(
        None, description="list of honors and awards."
    )
    accomplishment_patents: Optional[list[Patent | str]] = Field(None, description="list of patents.")
    accomplishment_courses: Optional[list[AccomplishmentCourse]] = Field(
        None, description="list of courses completed."
    )
    accomplishment_projects: Optional[list[Project | str]] = Field(
        None, description="list of projects completed."
    )
    accomplishment_test_scores: Optional[list[TestScore | str]] = Field(
        None, description="list of test scores."
    )
    volunteer_work: Optional[list[VolunteerWork]] = Field(
        None, description="list of volunteer work experiences."
    )
    certifications: Optional[list[Certification]] = Field(
        None, description="list of certifications."
    )
    connections: Optional[int] = Field(None, description="Number of connections.")
    people_also_viewed: Optional[list[str | PersonView]] = Field(
        None, description="list of profiles also viewed."
    )
    recommendations: Optional[list[Recommendation | str]] = Field(
        None, description="list of recommendations received."
    )
    activities: Optional[list[Activity]] = Field(None, description="list of activities.")
    similarly_named_profiles: Optional[list["Profile"]] = Field(
        None, description="list of profiles with similar names."
    )
    articles: Optional[list[Article]] = Field(None, description="list of articles.")
    groups: Optional[list[str | Group]] = Field(
        None, description="list of groups the profile is associated with."
    )
    skills: Optional[list[Skill | str]] = Field(None, description="list of skills.")
    inferred_salary: Optional[InferredSalary] = Field(None, description="Inferred salary range.")
    gender: Optional[str] = Field(None, description="Gender of the profile owner.")
    birth_date: Optional[Date | str] = Field(None, description="Birth date of the profile owner.")
    industry: Optional[str] = Field(None, description="Industry of work.")
    extra: Optional[dict] = Field(None, description="Additional information.")
    interests: Optional[list[str]] = Field(None, description="list of interests.")
    personal_emails: Optional[list[str]] = Field(
        None, description="list of personal email addresses."
    )
    personal_numbers: Optional[list[str]] = Field(
        None, description="list of personal phone numbers."
    )

    _parent: Optional["Response"] = PrivateAttr(None)
