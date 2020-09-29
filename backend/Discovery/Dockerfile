FROM openjdk:8-jdk-alpine

VOLUME /a402

COPY backend/Discovery/target/*.jar discovery.jar

ENTRYPOINT ["java", "-jar", "discovery.jar"]