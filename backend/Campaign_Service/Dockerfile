FROM openjdk:8-jdk-alpine

VOLUME /a402

COPY backend/Campaign_Service/target/*.jar campaign.jar

ENTRYPOINT ["java", "-jar", "campaign.jar"]