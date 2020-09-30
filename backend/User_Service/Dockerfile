FROM openjdk:8-jdk-alpine

VOLUME /a402

COPY backend/User_Service/target/*.jar user.jar

ENTRYPOINT ["java", "-jar", "user.jar"]